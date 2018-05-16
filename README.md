# WSU Environment Configuration

The purpose of this project is to provide unified software dependency support for students.

Python 3 is used for the entirety term.


## 1. [Git](https://git-scm.com/) Installation

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Git also provides Linux-like shell, Git Bash, to execute command easier than Windows Command Line tool.

### Setup Git
- [Download](https://git-scm.com/download/) the version compatible to your operating system.
- Using `default` option when installing.
- Make sure `Git Bash Here` is selected.
- After installation, you should have `Git Bash` installed.
- Launch `Git Bash`, and in the prompted window, type:
```sh
git --version
```
- You should see something like:
```sh
git version 2.17.0.windows.1
```

## 2. [Anaconda](https://www.anaconda.com/) Environment Setup
### 2.1 Overview
Using Anaconda consists of the following:

1. Install `[anaconda]`(https://www.anaconda.com/download/) on your computer
2. Create a new `[conda environment]`(http://conda.pydata.org/docs/using/envs.html) using this project
3. Each time you wish to work, activate your `conda` environment

### 2.2 Download and Installation
- [Download](https://www.anaconda.com/download/) the version compatible to your operating system.
- Choose `Python 3.6` version.
- Make sure you select the option `Add Anaconda to system PATH environment variable`.
- After installation, `conda` is added to your system.
- Launch `Git Bash`, and in the prompted window, type:
```sh
conda --version
```
- You should see something like:
```sh
conda 4.5.4
```
- Check if `Python 3.6` is installed, type in bash:
```sh
python --version
```
- You should see something like:
```sh
Python 3.6.1 :: Anaconda custom (64-bit)
```

### 2.3 Configure Conda Environment
For easy management, we put all the important files on your desktop.
- Go to your Windows desktop, if your are using Mac, launch terminal and `cd` to your desktop.
- Right click on desktop and select `Git Bash Here`, you should see `Bash` window prompts.

**Setup** the `wsu-adas` environment. 
```sh
git clone https://github.com/hxw0109/WSU.git
cd WSU
ls
```

**Create** wsu-adas.  Running this command will create a new `conda` environment that is provisioned with all libraries you need to be successful in this program.
```
conda env create -f environment.yml
```

*Note*: Some Mac users have reported issues installing TensorFlow using this method. The cause is unknown but seems to be related to `pip`. For the time being, we recommend opening environment.yml in a text editor and swapping
```yaml
    - tensorflow==0.12.1
```
with
```yaml
    - https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.1-py3-none-any.whl
```

**Verify** that the carnd-term1 environment was created in your environments:

```sh
conda info --envs
```

**Cleanup** downloaded libraries (remove tarballs, zip files, etc):

```sh
conda clean -tp
```

### 2.4 Uninstalling 

To uninstall the environment:

```sh
conda env remove -n wsu-adas
```

---



## Trouble Shooting

