# Port Forwarding Bypass

## Overview
This project provides a solution for scenarios where ISPs do not offer static IPs or charge for them. The tool utilizes a Discord bot to manage remote server interactions, handle file operations, and execute commands securely.

## Features
- **SSH Terminal Access:** Connect to a remote server and execute commands through a Discord bot.
- **File Upload and Download:** Upload files to the remote server and retrieve files from it.
- **Command Execution:** Run commands on the remote server directly from Discord.

## Setup
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Then, install the required Python packages:
   ```bash
   pip install py-cord python-dotenv
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory of the project with the following content:
   ```env
   TOKEN=your_discord_bot_token
   ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

## Commands
- **SSH Command:**
  - `/ssh` - Activate or deactivate the SSH terminal.
- **File Upload:**
  - `/upload_file <file> [relative_path]` - Upload a file to the remote server. Optionally specify a relative path.
- **File Retrieval:**
  - `/get_file <relative_path>` - Retrieve a file from the remote server by specifying the relative path.
- **Custom Command Execution:**
  - `,pi <command>` - Execute a command on the remote server and return the output.

## Example Usage
- To activate the SSH terminal:
  ```
  /ssh
  ```
- To upload a file:
  ```
  /upload_file <file> [relative_path]
  ```
- To retrieve a file:
  ```
  /get_file <relative_path>
  ```
- To execute a command:
  ```
  ,pi <command>
  ```

## Future Improvements
- **Config File:** Add support for a configuration file to customize bot settings and commands.
- **Aliases Support:** Implement command aliases to simplify frequently used commands.

## Contributing
Feel free to submit issues and pull requests. Contributions are welcome!
