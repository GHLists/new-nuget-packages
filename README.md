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

## Latest list — 2026-10-08 23:20 UTC

New packages created between 2026-10-08 22:19 UTC and 2026-10-08 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T23-20-06-991322Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 22:30:54 | [Luminy](https://www.nuget.org/packages/Luminy) | 1.0.1 | Samuel Alexandre Vidal | Math and Scientific reports in SVG/Html with zero-dependency |
| 2026-10-08 22:39:06 | [Barisozy.CleanArchitecture.Template](https://www.nuget.org/packages/Barisozy.CleanArchitecture.Template) | 1.1.3 | barisozy | A .NET 10 Clean Architecture API solution template. |
| 2026-10-08 22:40:19 | [Phoney](https://www.nuget.org/packages/Phoney) | 0.1.0 | Mattias Sundström | Fast, easy and flexible fake data for .NET: 77 locales imported from faker.js,… |
| 2026-10-08 22:42:09 | [Larroy.Kokoro.runtime.win-arm64](https://www.nuget.org/packages/Larroy.Kokoro.runtime.win-arm64) | 0.1.0 | larroy | kokoro.dll for win-arm64 (ONNX Runtime: Microsoft.ML.OnnxRuntime). Used by Larr… |
| 2026-10-08 22:42:10 | [Larroy.Kokoro.runtime.win-x64](https://www.nuget.org/packages/Larroy.Kokoro.runtime.win-x64) | 0.1.0 | larroy | kokoro.dll for win-x64 (ONNX Runtime: Microsoft.ML.OnnxRuntime). Used by Larroy… |
| 2026-10-08 22:42:12 | [Larroy.Kokoro.runtime.win-x64.cuda](https://www.nuget.org/packages/Larroy.Kokoro.runtime.win-x64.cuda) | 0.1.0 | larroy | Optional CUDA support for Larroy.Kokoro on win-x64 via Microsoft.ML.OnnxRuntime… |
| 2026-10-08 22:42:14 | [Larroy.Kokoro](https://www.nuget.org/packages/Larroy.Kokoro) | 0.1.0 | larroy | Kokoro TTS (kokoro.cpp) for .NET: managed wrapper over the kokoro C API. Native… |
| 2026-10-08 22:43:00 | [Brack.NET](https://www.nuget.org/packages/Brack.NET) | 1.0.0 | hsshss | .NET binding of brack.dll (libbrack.so on Linux, libbrack.dylib on macOS): host… |
| 2026-10-08 22:44:15 | [Trellis.Asp.Templates](https://www.nuget.org/packages/Trellis.Asp.Templates) | 1.0.151-alpha | Xavier John | A dotnet new template for creating ASP.NET services using the Trellis framework… |
| 2026-10-08 23:03:43 | [JB.UIConfigManager](https://www.nuget.org/packages/JB.UIConfigManager) | 1.0.40 | John Bell | Metadata driven forms display, field loading and saving with form templates |
| 2026-10-08 23:13:54 | [NovaCore.Agents.Browser](https://www.nuget.org/packages/NovaCore.Agents.Browser) | 4.0.0 | NovaCore | Browser use for NovaCore.Agents with any model: the library's browser tools ove… |
| 2026-10-08 23:13:56 | [NovaCore.Agents.Browser.LiveView](https://www.nuget.org/packages/NovaCore.Agents.Browser.LiveView) | 4.0.0 | NovaCore | Transport-neutral live-view primitives for NovaCore.Agents browser sessions: sc… |
| 2026-10-08 23:13:57 | [NovaCore.Agents.ComputerUse](https://www.nuget.org/packages/NovaCore.Agents.ComputerUse) | 4.0.0 | NovaCore | Native computer use for NovaCore.Agents: the OpenAI computer tool and the Anthr… |
| 2026-10-08 23:13:58 | [NovaCore.Agents.Hosting](https://www.nuget.org/packages/NovaCore.Agents.Hosting) | 4.0.0 | NovaCore | Optional hosting layer for NovaCore.Agents: durable sessions, conversation stor… |
| 2026-10-08 23:13:59 | [NovaCore.Agents.Hosting.EntityFramework](https://www.nuget.org/packages/NovaCore.Agents.Hosting.EntityFramework) | 4.0.0 | NovaCore | EF Core conversation store for NovaCore.Agents.Hosting, with its own tables inc… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
