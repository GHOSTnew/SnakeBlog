import subprocess


def git_revision():
    try:
        head = subprocess.Popen("git rev-parse --short HEAD",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, err = head.communicate()
        if out is not None:
            return out
        else:
            return "???"
    except:
        return "???"

GITREVISION = git_revision()
