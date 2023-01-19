"""
Using Popen class and exceptions handling
"""
import subprocess
from getpass import getpass
from pwinput import pwinput


def simple():
    print("=========OK")
    try:
        proc = subprocess.Popen(["python", "child.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs, errors = proc.communicate(timeout=15)
        print(f"returned code is: {proc.returncode}")
        print(f"outputs: \n{outputs.decode('utf-8')}\n")
        print(f"errors:\n{errors.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


def wrong_executable():
    print("=========wrong_executable")
    try:
        proc = subprocess.Popen(["wrong_executable", "child.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs, errors = proc.communicate(timeout=15)
        print(f"returned code is: {proc.returncode}")
        print(f"outputs: \n{outputs.decode('utf-8')}\n")
        print(f"errors:\n{errors.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


def file_not_found():
    print("=========file_not_found")
    try:
        proc = subprocess.Popen(["python", "notfound.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs, errors = proc.communicate(timeout=15)
        print(f"returned code is: {proc.returncode}")
        print(f"outputs: \n{outputs.decode('utf-8')}\n")
        print(f"errors:\n{errors.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


def request_sudo_passwd():
    """
    Important pipe stdin to pass password
    :return:
    """
    print("=========request_sudo_passwd")
    try:
        proc = subprocess.Popen(["sudo", "-S", "python", "child.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs, errors = proc.communicate(getpass("Please enter your password: ").encode(), timeout=15)
        print(f"returned code is: {proc.returncode}")
        print(f"outputs: \n{outputs.decode('utf-8')}\n")
        print(f"errors:\n{errors.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


def request_masked_sudo_passwd():
    """
    Important pipe stdin to pass password
    :return:
    """
    print("=========request_sudo_passwd")
    try:
        proc = subprocess.Popen(["sudo", "-S", "python", "child.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs, errors = proc.communicate(pwinput("please enter your password: ").encode(), timeout=15)
        print(f"returned code is: {proc.returncode}")
        print(f"outputs: \n{outputs.decode('utf-8')}\n")
        print(f"errors:\n{errors.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


if __name__ == '__main__':
    simple()
    wrong_executable()
    file_not_found()
    request_sudo_passwd()
    request_masked_sudo_passwd()
