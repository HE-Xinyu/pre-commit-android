# pre-commit-android
pre-commit hooks for Android Kotlin

# Motivation
As a nerd coder, I would like my code to be as clean as possible. 
Although Android Studio has the neat feature that [can automatically format all the 
files for me](https://stackoverflow.com/questions/40926920/reformat-whole-project-files-in-android-studio),
it has several drawbacks:

- It is impossible for me to do it **manually** before every commit.
- It does not follow the [Android Kotlin style guide](https://developer.android.com/kotlin/style-guide) carefully.
See below for details.

Hence I build a truly automatic tool based on [pre-commit](https://pre-commit.com/) that can:
- Check the code base against the style guide every time before committing
- Autofix issues that is trivial to fix
- Easy to install, no need to maintain it afterwards

# Prerequisites
The code formatter it runs is [ktlint](https://github.com/pinterest/ktlint). 
Don't worry, you don't need to download it manually. However, you need to make 
sure that `java` can be directly executed (i.e. its path is put in the system `PATH`
variable). To get the path, goto `File -> Project Structure -> JDK location` in
your Android Studio, and append a `bin` directory to it, e.g. 
`C:\Program Files\Android\Android Studio\jre\bin` on Windows. 

Open a **new** shell and run `java -version` to assure it works.


# Installation
1. Install [pre-commit](https://pre-commit.com/#install)
2. Create a file named `.pre-commit-config.yaml` in the **root** directory of your git repo.
3. Add the following content to it:
    ```yaml
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-xml
    -   repo: https://github.com/HE-Xinyu/pre-commit-android
        rev: master
        hooks:
        -   id: kotlin-formatter
    ```
4. Run `pre-commit install`

And you are good to go :). The hook will be triggered before every commit.
You can also run `pre-commit run --all-files` to manually do it if needed.

# Miscellaneous
- At the first time the hook starts, it will automatically download `ktlint`. It 
may take a while. The downloaded file is cached for further use. If the download 
failed due to network issues, simply retry.
- When at least 5 names used in a package, Android Studio will automatically
collapsed it using wildcard import (e.g. `import kotlinx.coroutines.*`). However,
it is against the [style guide](https://developer.android.com/kotlin/style-guide#import_statements).
To change this default behavior, goto `Settings -> Editor -> Code Style -> Kotlin -> Imports`, 
choose `Use single name import` and uncheck the `Packages to Use Import with '*'` boxes.

# License
[MIT](https://opensource.org/licenses/MIT)
