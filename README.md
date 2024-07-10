## Port Forwarding Bypass w/ a Discord bot

### Overview
This Discord bot helps bypass restrictions imposed by ISPs on port forwarding, which often require static IP requests. It allows remote interaction with a Raspberry Pi or similar device to manage files and execute commands.

### Features
- **SSH Terminal Access**: Connects to a remote device via SSH, providing terminal-like functionality within Discord.
- **File Upload**: Enables uploading files from Discord to the remote server.
- **Command Execution**: Executes shell commands on the remote device and displays output directly in Discord.

### Usage
1. **Commands**:
   - `,pi <command>`: Execute a command on the connected device via SSH.
   - `/ssh`: Activate SSH terminal for remote access (restricted to authorized users).
   - `/upload_file <file>`: Upload a file to the connected device (restricted to authorized users).

2. **Terminal Interaction**:
   - Use commands like `cd <directory>` to navigate the file system.
   - Execute any shell command supported by the remote device.

### Configuration
- **Environment Variables**: Ensure to set `TOKEN` in your `.env` file for bot authentication.
- **Configurations**: Future updates will include `config.json` for managing authorized users, servers, and banned commands.

### Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up environment variables in `.env`.

### Notes
- Ensure the bot is deployed in a secure environment, limiting access to authorized users.
- Monitor usage to prevent misuse or security breaches.

### Future Enhancements
- Implement `config.json` for better management of authorized users, banned commands, and server settings.
- Enhance error handling and user feedback for better usability.
