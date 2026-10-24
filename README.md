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

## Latest list — 2026-10-24 15:21 UTC

New packages created between 2026-10-24 14:20 UTC and 2026-10-24 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T15-21-42-041738Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 14:25:02 | [MultiPlug.Ext.ModbusTCP](https://www.nuget.org/packages/MultiPlug.Ext.ModbusTCP) | 0.0.1 | 4IR.UK | Use Modbus TCP with this MultiPlug Extension |
| 2026-10-24 14:47:45 | [Squora.Forms.Blazor.MudBlazorComponents](https://www.nuget.org/packages/Squora.Forms.Blazor.MudBlazorComponents) | 1.1.0 | Squora | MudBlazor implementation of the Squora Forms Blazor components. |
| 2026-10-24 14:47:45 | [Squora.Forms.Ai.Mcp](https://www.nuget.org/packages/Squora.Forms.Ai.Mcp) | 1.1.0 | Squora | MCP (Model Context Protocol) adapter for SquoraForms Hub. Exposes form definiti… |
| 2026-10-24 14:47:46 | [Squora.Forms.Blazor.Extensions](https://www.nuget.org/packages/Squora.Forms.Blazor.Extensions) | 1.1.0 | Squora | Dependency-injection registration (`AddSquoraForms`) and component registry for… |
| 2026-10-24 14:47:46 | [Squora.Forms.Blazor.SyncfusionComponents](https://www.nuget.org/packages/Squora.Forms.Blazor.SyncfusionComponents) | 1.1.0 | Squora | Syncfusion implementation of the Squora Forms Blazor components. Requires your… |
| 2026-10-24 14:47:47 | [Squora.Forms.Blazor.Actions](https://www.nuget.org/packages/Squora.Forms.Blazor.Actions) | 1.1.0 | Squora | Form action components (submit, reset, custom actions) for Squora Forms on Blaz… |
| 2026-10-24 14:47:47 | [Squora.Forms.Core](https://www.nuget.org/packages/Squora.Forms.Core) | 1.1.0 | Squora | Framework-neutral form model, rules engine and parsing for Squora Forms. No Bla… |
| 2026-10-24 14:47:47 | [Squora.Forms.UISchema](https://www.nuget.org/packages/Squora.Forms.UISchema) | 1.1.0 | Squora | UI Schema model, builders and converters describing how a form is laid out in S… |
| 2026-10-24 14:47:48 | [Squora.Forms.Common](https://www.nuget.org/packages/Squora.Forms.Common) | 1.1.0 | Squora | Shared enums and helpers used by the Squora Forms packages. |
| 2026-10-24 14:47:48 | [Squora.Forms.Blazor](https://www.nuget.org/packages/Squora.Forms.Blazor) | 1.1.0 | Squora | Blazor renderer base for Squora Forms: form component, layout and state service… |
| 2026-10-24 14:47:49 | [Squora.Forms.Contracts](https://www.nuget.org/packages/Squora.Forms.Contracts) | 1.1.0 | Squora | Interfaces for Squora Forms schema and scope providers. |
| 2026-10-24 14:47:49 | [Squora.Forms.Blazor.HtmlComponents](https://www.nuget.org/packages/Squora.Forms.Blazor.HtmlComponents) | 1.1.0 | Squora | Plain HTML implementation of the Squora Forms Blazor components. No third-party… |
| 2026-10-24 14:47:49 | [Squora.Forms.JsonSchema](https://www.nuget.org/packages/Squora.Forms.JsonSchema) | 1.1.0 | Squora | JSON Schema generation and handling for Squora Forms. |
| 2026-10-24 14:47:50 | [Squora.Forms.Ai.OpenAiTools](https://www.nuget.org/packages/Squora.Forms.Ai.OpenAiTools) | 1.1.0 | Squora | OpenAI and Anthropic tool definition generator for SquoraForms Hub forms. Auto-… |
| 2026-10-24 14:47:50 | [Squora.Forms.Blazor.RadzenComponents](https://www.nuget.org/packages/Squora.Forms.Blazor.RadzenComponents) | 1.1.0 | Squora | Radzen implementation of the Squora Forms Blazor components. |
| 2026-10-24 14:47:51 | [Squora.Forms.Blazor.Components](https://www.nuget.org/packages/Squora.Forms.Blazor.Components) | 1.1.0 | Squora | Abstract Blazor field and layout components that the Squora Forms UI framework… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
