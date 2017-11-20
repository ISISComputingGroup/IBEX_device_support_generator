""" Utilities common to all steps """
from git_utils import RepoWrapper
import logging
import subprocess
from os import access, chmod, W_OK, devnull
from stat import S_IWUSR
from shutil import rmtree as shutil_rmtree


def create_component(device, branch, path, action, commit_message, **kwargs):
    """
    Creates part of the IBEX device support
    :param device: Name of the device used in the action
    :param branch: Branch name to put the changes on
    :param path: Path to the repository
    :param action: Function that takes the device as an argument that creates the component
    :param commit_message: Message to attach to the changes
    """
    try:
        # repo = RepoWrapper(path)
        # repo.prepare_new_branch(branch)
        action(device, **kwargs)
        # repo.push_all_changes(commit_message)
    except (RuntimeError, IOError) as e:
        logging.error(str(e))
        return
    except RuntimeWarning as e:
        logging.warning(str(e))
    except Exception as e:
        logging.error("Encountered unknown error: {}".format(e))
        return


def run_command(command, working_dir):
    """
    Runs a command using subprocess. Waits for completion
    :param command: A list defining the command to run
    :param working_dir: The directory to run the command in
    """
    logging.info("Running command: {}".format(" ".join(command)))
    with open(devnull, 'w') as null_out:
        cmd = subprocess.Popen(command, cwd=working_dir, stdout=null_out, stderr=subprocess.STDOUT,
                               stdin=subprocess.PIPE)
    cmd.wait()


def replace_in_file(target, substitutions):
    logging.info("Making substitutions into file {}: {}".format(target, substitutions))
    with open(target) as f:
        lines = f.readlines()

    def substitute(input_str):
        output_str = input_str
        for s in substitutions:
            output_str = output_str.replace(s[0], s[1])
        return output_str

    with open(target, "w") as f:
        f.writelines(substitute(line) for line in lines)


def rmtree(delete_path):
    logging.info("Deleting folder {}".format(delete_path))
    def onerror(func, path, exc_info):
        if not access(path, W_OK):  # Is the error an access error ?
            chmod(path, S_IWUSR)
            func(path)
        else:
            raise
    shutil_rmtree(delete_path, onerror=onerror)