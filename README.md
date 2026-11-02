# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 01:19 UTC

New packages created between 2026-11-02 00:19 UTC and 2026-11-02 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T01-19-29-25378Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 00:51:13 | [Moka.AI.McpServer](https://www.nuget.org/packages/Moka.AI.McpServer) | 0.6.0 | jacobwi, BCat, Moka | Host an MCP server from Moka.AI — expose the tools registered in AiChatOptions.… |
| 2026-11-02 00:58:30 | [Scotec.Smtp.Service.Test](https://www.nuget.org/packages/Scotec.Smtp.Service.Test) | 2.0.1 | Scotec.Smtp.Service.Test | Package Description |
| 2026-11-02 01:08:26 | [Ai.Tlbx.VoiceAssistant.Telnyx](https://www.nuget.org/packages/Ai.Tlbx.VoiceAssistant.Telnyx) | 11.7.3 | TLBX | Telnyx REST provisioning, call control, signed ASP.NET Core webhooks and bidire… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
