import os
import signal
import subprocess
import requests

from Testing_framework.framework.resources.helpers.logger import logger

class LinuxOs:
    def __init__(self):
        pass

    def create_directory(self, directory_path):
        """Creates a new directory.
        Args:
            directory_path (str): The full path of the directory to create.
        """
        try:
            os.makedirs(directory_path)
            logger.info(f"Directory {directory_path} created successfully.")
        except OSError as error:
            logger.error(f"Error creating directory: {error}")

    def kill_process(self, process_name):
        """Kills a process given its process_name.
        Args:
            process_name (str): The process NAME to terminate.
        """
        pid = self._find_pid_by_name(process_name= process_name)
        try:
            os.kill(pid, signal.SIGTERM)
            logger.info(f"Process with Process name {process_name} and PID {pid} terminated.")
        except ProcessLookupError:
            logger.error(f"Process with PID {pid} not found.")
        except OSError as error:
            logger.error(f"Error terminating process: {error}")
    
    def _find_pid_by_name(self, process_name):
        """Finds the PID of a process given its name.
        Args:
            process_name (str): The name of the process to search for.
        Returns:
            list: A list of PIDs matching the process, or an empty list if not found.
        This method uses the `ps` command to list all processes and then filters
        the output based on the process name. It excludes the grep process itself
        from the results.
        """
        cmd = f"ps aux | grep {process_name} | grep -v grep | awk '{{print $2}}'"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True)
            pids = output.splitlines()
            return pids
        except subprocess.CalledProcessError as e:
            logger.error(f"Error finding PID: {e}")
            return pids
        
    def download_file(self, url, destination):
        """
        Downloads a file from the given URL to the specified destination.
        Args:
        url (str): The URL of the file to download.
        destination (str): The local path where the file will be saved.
        """
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(destination, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):

                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            logger.info(f"File downloaded to {destination}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error downloading file: {e}")
    
    def as_sudo(self, command):
        """
        Executes a command with sudo privileges.
        Args:
            command (str): The command to execute as sudo.
        Returns:
            str: The output of the command.
        """
        try:
            output = subprocess.check_output(['sudo', command], text=True)
            return output
        except subprocess.CalledProcessError as e:
            logger.error(f"Error executing command as sudo: {e}")
            return None

    def remove_dir(self, directory_path):
        """Removes a directory and its contents.
        Args:
            directory_path (str): The path to the directory to remove.
        """
        try:
            os.rmdir(directory_path)
            logger.info(f"Directory {directory_path} removed.")
        except OSError as error:
            logger.error(f"Error removing directory: {error}")

    def is_file_exist(self, file_path):
        """Checks if a file exists.
        Args:
            file_path (str): The path to the file.
        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(file_path)

    def is_folder_exist(self, folder_path):
        """Checks if a folder exists.
        Args:
            folder_path (str): The path to the folder.
        Returns:
            bool: True if the folder exists, False otherwise.
        """
        return os.path.isdir(folder_path)

    def is_file_empty(self, file_path):
        """Checks if a file is empty.
        Args:
            file_path (str): The path to the file.
        Returns:
            bool: True if the file is empty, False otherwise.
        """
        return os.path.getsize(file_path) == 0

    def is_folder_empty(self, folder_path):
        """Checks if a folder is empty.
        Args:
            folder_path (str): The path to the folder.
        Returns:
            bool: True if the folder is empty, False otherwise.
        """
        try:
            for _, _, files in os.walk(folder_path):
                if files:
                    return False
            return True
        except OSError:
            return False

    def clear_folder(self, folder_path):
        """Removes all files and subdirectories from a folder.
        Args:
            folder_path (str): The path to the folder.
        """
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))