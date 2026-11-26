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

## Latest list — 2026-11-26 21:20 UTC

New packages created between 2026-11-26 20:20 UTC and 2026-11-26 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T21-20-30-140386Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 20:24:52 | [Frazex.BotFlowEngine.DependencyInjection](https://www.nuget.org/packages/Frazex.BotFlowEngine.DependencyInjection) | 0.1.0 | Frazex-LLC | Microsoft.Extensions.DependencyInjection integration for FlowEngine: RegisterFl… |
| 2026-11-26 20:25:48 | [Eternet.Testing.Build](https://www.nuget.org/packages/Eternet.Testing.Build) | 1.0.0 | Eternet | Build props for Eternet test projects: xUnit v3 on Microsoft.Testing.Platform w… |
| 2026-11-26 20:27:11 | [IINET.UI.Calendar](https://www.nuget.org/packages/IINET.UI.Calendar) | 0.1.0 | Ilya | Настраиваемый элемент управления Calendar для Avalonia UI с поддержкой произвол… |
| 2026-11-26 20:28:01 | [BitMagic.X16Basic.Debugger](https://www.nuget.org/packages/BitMagic.X16Basic.Debugger) | 0.1.0 | Yazwh0 | Debugs Commander X16 BASIC in X16D. |
| 2026-11-26 20:28:01 | [BitMagic.X16Basic](https://www.nuget.org/packages/BitMagic.X16Basic) | 0.1.0 | Yazwh0 | Commander X16 BASIC: tokeniser, detokeniser, source maps and decoders for BASIC… |
| 2026-11-26 20:28:29 | [DomeMQ.Client](https://www.nuget.org/packages/DomeMQ.Client) | 0.1.0 | Hannes Hold | Client library for the DomeMQ IPC message broker. No third-party dependencies. |
| 2026-11-26 20:28:29 | [DomeMQ.Protocol](https://www.nuget.org/packages/DomeMQ.Protocol) | 0.1.0 | Hannes Hold | Frame codec, message bodies, and transport abstractions for the DomeMQ IPC prot… |
| 2026-11-26 20:28:30 | [DomeMQ.Server](https://www.nuget.org/packages/DomeMQ.Server) | 0.1.0 | Hannes Hold | Embeddable DomeMQ broker. No third-party dependencies. |
| 2026-11-26 20:40:15 | [Saraff.TwainX](https://www.nuget.org/packages/Saraff.TwainX) | 1.0.34 | Copyright © SARAFF 2011 | Allows you to control work of flatbed scanner, web and digital camera and any o… |
| 2026-11-26 20:42:59 | [Cosmos.OpenTelemetry.Wolverine](https://www.nuget.org/packages/Cosmos.OpenTelemetry.Wolverine) | 0.1.0 | Cosmos | Contexto de traza W3C en los mensajes que publica Wolverine: escribe traceparen… |
| 2026-11-26 20:44:10 | [Clockworks.CLX.Protocol](https://www.nuget.org/packages/Clockworks.CLX.Protocol) | 0.1.0 | Clockworks | Receive a live CLX stream from Clockworks senders in any .NET app: deck time, t… |
| 2026-11-26 20:45:54 | [clc-authentication](https://www.nuget.org/packages/clc-authentication) | 1.0.0 | Central Library Consortium | Microsoft Entra ID sign-in and CLC membership authorization for ASP.NET Core we… |
| 2026-11-26 20:53:45 | [Compze.Threading.Interprocess.MemoryPack](https://www.nuget.org/packages/Compze.Threading.Interprocess.MemoryPack) | 0.7.0-alpha | Lidbom Solutions AB | MemoryPack serialization for the IInterprocessObject of Compze.Threading.Interp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
