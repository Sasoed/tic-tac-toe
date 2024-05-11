#!/bin/bash

: <<'DESCRIPTION'

A tool to run tests automatically when a file is changed or key is pressed.

Requirements (macOS):

    brew install fswatch
    python3 (usually found in virtual env)

Works best with iTerm2, because it can change the color of the tab depending on results.


Usage:

    1. Start ./tests_watch.sh
    2. Observe tests results
    3. Modify source code
    4. Tests are run automatically when file is saved
    5. Go to 2.


Useful pytest options:

    ./tests_watch.sh some_app
    ./tests_watch.sh some_app/tests_some_feature.py
    ./tests_watch.sh some_app/tests_some_feature.py::test_some_aspect
    ./tests_watch.sh -n 0
    ./tests_watch.sh --ff
    ./tests_watch.sh --lf
    ./tests_watch.sh -x
    ./tests_watch.sh --create-db
    ./tests_watch.sh --migrations

DESCRIPTION

# Save arguments
args=$@

main() {
    # Run tests when the script first starts
    run_tests

    # Infinite loop that reruns tests
    while true; do
        echo "Press any key or change a Python file to run tests again. Press Ctrl+C to exit."

        monitor_changes

        if [ $? -ne 0 ]; then
            echo "Ctrl+C pressed, exiting"
            exit
        fi

        run_tests
    done
}


run_tests() {
    python -m pytest $args  && echo_ok || echo_fail
}

echo_ok() {
    ITERM_MAKE_TAB_GREEN="\033]6;1;bg;red;brightness;57\a\033]6;1;bg;green;brightness;197\a\033]6;1;bg;blue;brightness;77\a"
    echo -e "\033[0;32mok\033[0m$ITERM_MAKE_TAB_GREEN"
}

echo_fail() {
    ITERM_MAKE_TAB_RED="\033]6;1;bg;red;brightness;270\a\033]6;1;bg;green;brightness;60\a\033]6;1;bg;blue;brightness;83\a"
    echo -e "\033[0;31mfailed\033[0m$ITERM_MAKE_TAB_RED"
}

monitor_changes() {
    python -c "
'''
This program runs two commands simultaneously and waits for one of them to exit.
Then it kills the other one and exits with return code 0.

If it was interrupted with Ctrl+C, it exits with non-zero return code.

'''

import asyncio

commands = [
    'fswatch --one-event --exclude \".*\" --include=\"\\\\.py$\" .',
    '/usr/bin/read -rsn1 key',
]

def main():
    try:
        asyncio.run(wait_for_any_command(commands))
        exit(0)
    except KeyboardInterrupt:
        exit(-1)

async def run_subcommand(command):
    try:
        process = await asyncio.create_subprocess_shell(command)
        await process.wait()
    except asyncio.CancelledError:
        process.kill()

async def wait_for_any_command(commands):
    tasks = [asyncio.create_task(run_subcommand(command)) for command in commands]
    _, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()

main()
"

    return $?
}

main