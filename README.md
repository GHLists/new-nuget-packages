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

## Latest list — 2026-11-16 21:19 UTC

New packages created between 2026-11-16 20:18 UTC and 2026-11-16 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T21-19-42-408395Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 20:20:01 | [OpenUI.Lang.Blazor](https://www.nuget.org/packages/OpenUI.Lang.Blazor) | 1.1.0 | Dale Francis | Renders a live OpenUI Lang session in Blazor, under any render mode, with the c… |
| 2026-11-16 20:20:02 | [OpenUI.Lang.Blazor.Mud](https://www.nuget.org/packages/OpenUI.Lang.Blazor.Mud) | 9.11.0 | Dale Francis | Definitions and MudBlazor views for OpenUI Lang components, built against MudBl… |
| 2026-11-16 20:28:15 | [AWSSDK.ConnectScheduling](https://www.nuget.org/packages/AWSSDK.ConnectScheduling) | 4.1.0 | Amazon Web Services | The Amazon Web Services SDK for .NET - Amazon Connect Scheduling |
| 2026-11-16 20:31:59 | [AWSSDK.SageMakerInferenceRouterRuntime](https://www.nuget.org/packages/AWSSDK.SageMakerInferenceRouterRuntime) | 4.1.0 | Amazon Web Services | The Amazon Web Services SDK for .NET - Amazon SageMaker Inference Router Runtime |
| 2026-11-16 20:32:14 | [IECode.Cli](https://www.nuget.org/packages/IECode.Cli) | 0.2.17 | Jan Junklewitz and the IECode… | iecode: TwinCAT 3 engineering from the command line (build, activate, libraries… |
| 2026-11-16 20:32:28 | [AWSSDK.OpenSearchMemory](https://www.nuget.org/packages/AWSSDK.OpenSearchMemory) | 4.1.0 | Amazon Web Services | The Amazon Web Services SDK for .NET - Amazon OpenSearch Memory |
| 2026-11-16 20:36:07 | [GM.Messaging.AspNetCore](https://www.nuget.org/packages/GM.Messaging.AspNetCore) | 4.2.0 | Giorgi Metskhvarishvili | ASP.NET Core endpoints for operating GM.Messaging: MapGMMessagingAdmin() maps t… |
| 2026-11-16 20:41:40 | [EetKit](https://www.nuget.org/packages/EetKit) | 0.1.0 | Bedřich Malý | Odesílání tržeb do EET 2.0 (rozhraní v4.1): validace, podpis WS-Security, odesl… |
| 2026-11-16 20:41:41 | [EetKit.Extensions.DependencyInjection](https://www.nuget.org/packages/EetKit.Extensions.DependencyInjection) | 0.1.0 | Bedřich Malý | Registrace EetKit do Microsoft.Extensions.DependencyInjection: services.AddEet(… |
| 2026-11-16 20:57:34 | [DigiTFactory.Libraries.Analyzers](https://www.nuget.org/packages/DigiTFactory.Libraries.Analyzers) | 0.1.0 | DigiTFactory.Libraries.Analyz… | Roslyn analyzers enforcing the DigiTFactory EDM quality gates (QG-*). |
| 2026-11-16 21:00:30 | [Grimoire.Consumer](https://www.nuget.org/packages/Grimoire.Consumer) | 2.1.0 | Guilherme Branco Stracini | .NET client for Grimoire, the self-hosted Vault & Configuration Manager. Load c… |
| 2026-11-16 21:01:46 | [DrawnUi.Blazor.Add3d](https://www.nuget.org/packages/DrawnUi.Blazor.Add3d) | 1.10.9.1 | Nick Kovalsky aka AppoMobi an… | 3D models in a DrawnUI screen for Blazor WebAssembly: glTF scenes with skeleton… |
| 2026-11-16 21:02:36 | [DrawnUi.Maui.Add3d](https://www.nuget.org/packages/DrawnUi.Maui.Add3d) | 1.10.9.1 | Nick Kovalsky aka AppoMobi an… | 3D models in a DrawnUI screen for .NET MAUI: glTF scenes with skeleton animatio… |
| 2026-11-16 21:03:08 | [DrawnUi.OpenTk.Add3d](https://www.nuget.org/packages/DrawnUi.OpenTk.Add3d) | 1.10.9.1 | Nick Kovalsky aka AppoMobi an… | 3D models in a DrawnUI screen with OpenTK on Windows and Linux: glTF scenes wit… |
| 2026-11-16 21:03:22 | [DrawnUi.Web.Add3d](https://www.nuget.org/packages/DrawnUi.Web.Add3d) | 1.10.9.1 | Nick Kovalsky aka AppoMobi an… | 3D models in a DrawnUI screen on pure WebAssembly (no Blazor): glTF scenes with… |
| 2026-11-16 21:03:34 | [DrawnUi.Wpf.Add3d](https://www.nuget.org/packages/DrawnUi.Wpf.Add3d) | 1.10.9.1 | Nick Kovalsky aka AppoMobi an… | 3D models in a DrawnUI screen inside a WPF window: glTF scenes with skeleton an… |
| 2026-11-16 21:03:44 | [GM.Testing.Messaging.Integration](https://www.nuget.org/packages/GM.Testing.Messaging.Integration) | 1.1.0 | Giorgi Metskhvarishvili | Integration-test kit for GM.Messaging services: MessagingContainers starts Post… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
