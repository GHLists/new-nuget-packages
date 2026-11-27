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

## Latest list — 2026-11-27 21:20 UTC

New packages created between 2026-11-27 20:20 UTC and 2026-11-27 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T21-20-31-733815Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 20:26:30 | [Browshot](https://www.nuget.org/packages/Browshot) | 2.0.1 | Browshot | C# client for the Browshot API. |
| 2026-11-27 20:36:02 | [Gtk.Windows.Forms.Automation](https://www.nuget.org/packages/Gtk.Windows.Forms.Automation) | 1.4.2464.26331 | Piero Viano | Drive the forms of a Gtk.Windows.Forms.Base application from code: show a form,… |
| 2026-11-27 20:36:04 | [Gtk.Windows.Forms.Automation.Xunit](https://www.nuget.org/packages/Gtk.Windows.Forms.Automation.Xunit) | 1.4.2464.26331 | Piero Viano | An xUnit v2 test framework that runs every test of an assembly on one dedicated… |
| 2026-11-27 20:36:23 | [Saraff.Twain.Aux.Contracts](https://www.nuget.org/packages/Saraff.Twain.Aux.Contracts) | 2.0.0 | SARAFF | Wire contracts for Saraff.Twain.Aux. |
| 2026-11-27 20:37:35 | [bottlenoselabs.Sdk](https://www.nuget.org/packages/bottlenoselabs.Sdk) | 2026.11.27-rc | bottlenoselabs | The MSBuild SDK for C# libraries and apps at Bottlenose Labs. Wraps Microsoft.N… |
| 2026-11-27 20:37:36 | [bottlenoselabs.Sdk.WebApp](https://www.nuget.org/packages/bottlenoselabs.Sdk.WebApp) | 2026.11.27-rc | bottlenoselabs | The MSBuild SDK for C# web apps at Bottlenose Labs. Wraps Microsoft.NET.Sdk.Web. |
| 2026-11-27 20:37:37 | [bottlenoselabs.Sdk.GameApp](https://www.nuget.org/packages/bottlenoselabs.Sdk.GameApp) | 2026.11.27-rc | bottlenoselabs | The MSBuild SDK for C# games at Bottlenose Labs. Wraps Microsoft.NET.Sdk. |
| 2026-11-27 20:37:37 | [bottlenoselabs.Templates](https://www.nuget.org/packages/bottlenoselabs.Templates) | 2026.11.27-rc | bottlenoselabs | `dotnet new` templates for repositories on the bottlenoselabs.Sdk MSBuild SDKs:… |
| 2026-11-27 20:50:25 | [M0LTE.OfdmFm](https://www.nuget.org/packages/M0LTE.OfdmFm) | 0.1.0 | Tom Fanning M0LTE | An adaptive OFDM modem for the audio path of an FM radio, for .NET. Every burst… |
| 2026-11-27 20:56:57 | [Noggog.Build.Dev](https://www.nuget.org/packages/Noggog.Build.Dev) | 5.0.2 | Noggog | Shared local-development MSBuild targets for Noggog repos. Clears a freshly pac… |
| 2026-11-27 21:09:58 | [Surly.Surl.Api](https://www.nuget.org/packages/Surly.Surl.Api) | 0.1.12 | Stewart Scott Rogers | Starts and stops Surl servers in-process for a .NET test suite: Surl is the ser… |
| 2026-11-27 21:10:00 | [Surly.Surl.Mcp](https://www.nuget.org/packages/Surly.Surl.Mcp) | 0.1.12 | Stewart Scott Rogers | An MCP server whose tools let AI agents start, list and stop Surl protocol serv… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
