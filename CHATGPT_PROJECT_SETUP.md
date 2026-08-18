# ChatGPT Project Setup

Recommended project name: **WinLoop Continuation**

ChatGPT Projects are managed in the ChatGPT UI. This package cannot programmatically create a Project or move an existing chat into one.

## One-time UI setup

1. In the ChatGPT sidebar, choose **New project**.
2. Name it **WinLoop Continuation**.
3. Open this WinLoop continuation chat's `...` menu and choose **Move to project** (or drag the chat onto the project).
4. Add this ZIP or the extracted V42 files as project sources if desired.
5. Use the **WinLoop GitHub Continuation** scheduled task as the recurring automation.

Important: scheduled tasks cannot rely on Project file uploads as their runtime file source, so GitHub is configured as the durable source of truth for continuation runs.
