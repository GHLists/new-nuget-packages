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

## Latest list — 2026-11-21 22:18 UTC

New packages created between 2026-11-21 21:20 UTC and 2026-11-21 22:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T22-18-45-138995Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 21:27:33 | [SbsReport](https://www.nuget.org/packages/SbsReport) | 1.0.0 | Sobis | Modern, hızlı, Web Designer IDE ve Viewer destekli .sbs raporlama kütüphanesi (… |
| 2026-11-21 21:30:18 | [compujuckel.Serilog.Sinks.Journald](https://www.nuget.org/packages/compujuckel.Serilog.Sinks.Journald) | 1.0.1 | compujuckel | Serilog sink that writes log events to the systemd journal. |
| 2026-11-21 21:33:28 | [GrayMint.TlsCertificates](https://www.nuget.org/packages/GrayMint.TlsCertificates) | 1.0.1 | GrayMint | TLS certificates for the domains an app serves, from Let's Encrypt or another A… |
| 2026-11-21 21:37:19 | [TensorStack.OnnxRuntime.LLM](https://www.nuget.org/packages/TensorStack.OnnxRuntime.LLM) | 0.15.1 | sa_ddam213 | Text generation, speech recognition, text to speech and vision-language pipelin… |
| 2026-11-21 21:38:34 | [Nev.Core](https://www.nuget.org/packages/Nev.Core) | 1.0.0 | Chris Varley | Nev is a .NET library for fast, structured decision support. You can use it for… |
| 2026-11-21 21:49:09 | [Blazix.Primitives](https://www.nuget.org/packages/Blazix.Primitives) | 0.1.0 | Blazix | Unstyled, accessible Blazor primitives. Bring your own CSS. |
| 2026-11-21 21:49:10 | [Blazix.Cli](https://www.nuget.org/packages/Blazix.Cli) | 0.1.0 | Blazix | Copies Blazix's styled Blazor components into your project as source you own. |
| 2026-11-21 21:49:54 | [ZeroCSharp.Templates](https://www.nuget.org/packages/ZeroCSharp.Templates) | 0.1.0 | Zero C# contributors | dotnet new zero (a native program) and dotnet new zerolib (a library) for zero-… |
| 2026-11-21 21:49:57 | [ZeroCSharp.Bflat.linux-x64](https://www.nuget.org/packages/ZeroCSharp.Bflat.linux-x64) | 0.1.0 | Zero C# contributors | bflat (OnurGumus/bflat fork), trimmed to what Zero C# builds use, for linux-x64… |
| 2026-11-21 21:49:58 | [ZeroCSharp.Sdk](https://www.nuget.org/packages/ZeroCSharp.Sdk) | 0.1.0 | Zero C# contributors | Zero-mode C#: C# compiled to small native programs with no .NET runtime. Use as… |
| 2026-11-21 21:50:01 | [ZeroCSharp.Bflat.linux-arm64](https://www.nuget.org/packages/ZeroCSharp.Bflat.linux-arm64) | 0.1.0 | Zero C# contributors | bflat (OnurGumus/bflat fork), trimmed to what Zero C# builds use, for linux-arm… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
