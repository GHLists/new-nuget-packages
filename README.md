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

## Latest list — 2026-10-14 12:20 UTC

New packages created between 2026-10-14 11:20 UTC and 2026-10-14 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T12-20-15-769204Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 11:33:48 | [AwsSecrets](https://www.nuget.org/packages/AwsSecrets) | 1.0.0 | Qantler | AWS Secrets Manager helper library with appsettings fallback. |
| 2026-10-14 11:38:10 | [Fadenstack.Agents](https://www.nuget.org/packages/Fadenstack.Agents) | 0.2.0 | Emagin8 UG (haftungsbeschränk… | Agents on Fadenstack: the agent builder, the tool loop with host tools, tool mo… |
| 2026-10-14 11:38:23 | [Fadenstack.Client](https://www.nuget.org/packages/Fadenstack.Client) | 0.2.0 | Emagin8 UG (haftungsbeschränk… | The Fadenstack core client: an IChatClient for the gateway (agent-scoped or pla… |
| 2026-10-14 11:39:42 | [Fadenstack.Mcp](https://www.nuget.org/packages/Fadenstack.Mcp) | 0.2.0 | Emagin8 UG (haftungsbeschränk… | MCP for Fadenstack agents: local MCP servers as agent tools, under the agent's… |
| 2026-10-14 11:43:27 | [Fadenstack.UI](https://www.nuget.org/packages/Fadenstack.UI) | 0.2.0 | Emagin8 UG (haftungsbeschränk… | Platform-neutral view models for Fadenstack agents: the chat, streamed markdown… |
| 2026-10-14 11:43:47 | [Fadenstack.UI.Wpf](https://www.nuget.org/packages/Fadenstack.UI.Wpf) | 0.2.0 | Emagin8 UG (haftungsbeschränk… | The WPF skin for Fadenstack.UI: a chat panel for Fadenstack agents in WPF hosts… |
| 2026-10-14 11:50:53 | [Sa.Data.TempFolder](https://www.nuget.org/packages/Sa.Data.TempFolder) | 0.16.0 | dundich | Temporary directory management: path-guarded subfolders, debounced activity mar… |
| 2026-10-14 11:57:32 | [Samwizardry.ExpressionParser](https://www.nuget.org/packages/Samwizardry.ExpressionParser) | 1.0.0 | samwizardry | A lightweight string filter parser that compiles text expressions into strongly… |
| 2026-10-14 11:58:13 | [SesliOkuma.Engine](https://www.nuget.org/packages/SesliOkuma.Engine) | 2.0.0 | Koray Orhun | Read-aloud engine for Windows (.NET Framework 4.8, no UI framework): grabs the… |
| 2026-10-14 12:02:28 | [Esatto.Umbraco.Backoffice.TreeDragAndDrop](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.TreeDragAndDrop) | 1.0.0 | Carl Schéle | Drag-and-drop and keyboard "grab & place" moving for the Umbraco 17/18 backoffi… |
| 2026-10-14 12:04:19 | [MoeinSoft.TaxCollectData.Library](https://www.nuget.org/packages/MoeinSoft.TaxCollectData.Library) | 2.0.32 | Mostafa.Nazuri | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
