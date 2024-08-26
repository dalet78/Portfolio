import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, EMA, RSI
import json
from libs.filtered_stock import return_filtred_list
from datetime import time
import matplotlib.pyplot as plt
from Reports.report_builder import ReportGenerator
from Trading.methodology.PriceAction.sma_vwap_sr_support import SupportResistanceFinder

def load_data(filepath):
    """Carica i dati dal file CSV."""
    df = pd.read_csv(filepath, parse_dates=['Datetime'])
    df.rename(columns={'Datetime': 'datetime'}, inplace=True)
    df.set_index('datetime', inplace=True)
    return df


class HOLCStrategy(Strategy):
    last_trade_date = None
    def init(self):
        super().init()
        price = pd.Series(self.data.Close)
        self.rsi = self.I(RSI, price, 14)
        self.rsi_ma = self.I(SMA, self.rsi, 14)

    def next(self):
        current_time = self.data.index[-1].time()
        current_date = self.data.index[-1].date()

        entry_start_time = time(9, 30)
        entry_end_time = time(9, 40)
        exit_time = time(10, 10)

        rsi_value = self.rsi[-1]
        rsi_ma_value = self.rsi_ma[-1]
        candle_direction = "bullish" if self.data.Close[-1] > self.data.Open[-1] else "bearish"

        if self.position and current_time >= exit_time:
            self.position.close()
            self.last_trade_date = None

        elif entry_start_time <= current_time <= entry_end_time and (
                self.last_trade_date is None or self.last_trade_date != current_date):

            # Verifica il crossover tra RSI e la sua SMA
            if rsi_value > rsi_ma_value and self.rsi[-2] <= self.rsi_ma[-2] and candle_direction == "bullish":
                stop_loss = self.data.Low[-1] - 0.15
                take_profit = self.data.Close[-1] + 0.30
                self.buy(sl=stop_loss, tp=take_profit)

            # Verifica il crossunder tra RSI e la sua SMA
            elif rsi_value < rsi_ma_value and self.rsi[-2] >= self.rsi_ma[-2] and candle_direction == "bearish":
                stop_loss = self.data.High[-1] + 0.15
                take_profit = self.data.Close[-1] - 0.30
                self.sell(sl=stop_loss, tp=take_profit)

            self.last_trade_date = current_date



def rsi_cross_trading(index = "SP500"):
    global df
    source_directory = "/home/dp/PycharmProjects/Portfolio_management/Portfolio_management"
    report = ReportGenerator()
    report.add_title(title=f"{index}  10 min EMA- SMA crossing stock")

    with open(f"{source_directory}/Trading/methodology/strategy_parameter.json", 'r') as file:
        param_data = json.load(file)

        tickers_list = return_filtred_list(index=index)
        # Controlla se la lista dei ticker è vuota
        if not tickers_list:
            # Aggiungi un messaggio nel report o registra un log

            print("Nessun ticker soddisfa i criteri di selezione.")
        else:

            for item in tickers_list:
                print(f'Analyze stock = {item}')
                try:
                    data_filepath = f"{source_directory}/Data/{index}/5min/{item}_historical_data.csv"
                    df = load_data(data_filepath)

                    # Esegui il backtesting
                    bt = Backtest(df, HOLCStrategy, cash=10000, commission=.002,
                                exclusive_orders = True)
                    stats = bt.run()

                    total_trades = stats['_trades'].shape[0]
                    win_rate = stats['Win Rate [%]']

                    # Controlla se il stock soddisfa i criteri
                    if total_trades > 3 and win_rate > 50:
                        # Salva il grafico in una variabile
                        fig = bt.plot()
                        sr_support = SupportResistanceFinder(data=df)
                        list_sr = sr_support.find_levels()
                        report.add_content(f"stock = {item}")
                        # report.add_content(f"Optimal High_vwap_diff for {item}: {best_high_vwap_diff}")
                        report.add_content(f"Corresponding Win Rate: {win_rate}%")
                        report.add_content(f"total trade = {total_trades}\n")
                        report.add_content(f"support and resistance list: {list_sr} ")

                        # Aggiungi il nome dello stock come titolo del grafico
                        print(f'Performance del Backtest per {item} (Win Rate: {win_rate}%)')

                except FileNotFoundError:
                # Gestisci l'errore se il file non viene trovato
                    print(f"File non trovato per {item}")
                except Exception as e:
                # Gestisci altri errori generici
                    print(f"Errore durante l'elaborazione di {item}: {e}")
        file_report = report.save_report(filename=f"{index}_ema_cross_stock")
        return file_report

# Preparazione per il backtesting
if __name__ == "__main__":
    # rsi_cross_trading(index="Nasdaq")
    # rsi_cross_trading(index="Russel")
    rsi_cross_trading(index="SP500")

