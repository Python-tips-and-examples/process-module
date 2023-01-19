"""
Using subprocess run and exceptions handling
"""
import subprocess


def ok():
    print("=========OK")
    try:
        output = subprocess.run(["python", "child.py"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"returned code is: {output.returncode}\n"
              f"stdout content: \n{output.stdout.decode('utf-8')}")
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
        output = subprocess.run(["wrong_executable", "child.py"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"returned code is: {output.returncode}\n"
              f"stdout content: \n{output.stdout.decode('utf-8')}")
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
        output = subprocess.run(["python", "notfound.py"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"returned code is: {output.returncode}\n"
              f"stdout content: \n{output.stdout.decode('utf-8')}")
    except FileNotFoundError as e:
        print(f"Process failed because the executable could not be found: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Process failed because did not return a successful return code. "
              f"Returned {e.returncode}\n{e}\n{e.stderr.decode('utf-8')}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")


if __name__ == '__main__':
    ok()
    wrong_executable()
    file_not_found()