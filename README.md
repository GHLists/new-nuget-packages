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

## Latest list — 2026-09-30 21:19 UTC

New packages created between 2026-09-30 20:20 UTC and 2026-09-30 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T21-19-22-795393Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 20:20:55 | [Glacier.Agent](https://www.nuget.org/packages/Glacier.Agent) | 1.0.0 | Ian Cowley | Pure C# .NET 10 Autonomous Agent Runtime, SIMD Radix Trie Tokenizer (>50M tok/s… |
| 2026-09-30 20:22:01 | [Asteroid.GodotCli.CompilerTools](https://www.nuget.org/packages/Asteroid.GodotCli.CompilerTools) | 0.1.0 | Asteroid.GodotCli.CompilerToo… | Compile-time gates paired with the GodotCli tool declaration attributes. |
| 2026-09-30 20:23:33 | [Glacier.Windowing](https://www.nuget.org/packages/Glacier.Windowing) | 1.0.0 | Ian Cowley | Pure C# .NET 10 Cross-Platform Windowing, Hardware Swapchain (D3D12/Vulkan/Meta… |
| 2026-09-30 20:41:50 | [Itp.WpfCamera](https://www.nuget.org/packages/Itp.WpfCamera) | 3.0.1 | mgaffigan | Live preview and still capture from webcams in WPF applications, using WinRT Me… |
| 2026-09-30 20:47:13 | [ElBruno.LocalLLMs.Decisions](https://www.nuget.org/packages/ElBruno.LocalLLMs.Decisions) | 0.22.0 | Bruno Capuano (ElBruno) | Local System One decision models for ElBruno.LocalLLMs. Typed choice, score and… |
| 2026-09-30 20:48:16 | [Beryllium.LocalizationManager](https://www.nuget.org/packages/Beryllium.LocalizationManager) | 1.6.0 | Vladyslav Pysarenko | Localization manager for simple and efficient switching between languages. Read… |
| 2026-09-30 21:00:52 | [OpenApiFeatureFlags.Swashbuckle](https://www.nuget.org/packages/OpenApiFeatureFlags.Swashbuckle) | 0.1.0 | Dogukan Demir | Swashbuckle adapter for OpenApiFeatureFlags: hides gated operations, parameters… |
| 2026-09-30 21:00:53 | [OpenApiFeatureFlags.OpenFeature](https://www.nuget.org/packages/OpenApiFeatureFlags.OpenFeature) | 0.1.0 | Dogukan Demir | OpenFeature flag source for OpenApiFeatureFlags: reads flags through the CNCF v… |
| 2026-09-30 21:00:54 | [OpenApiFeatureFlags.FeatureManagement](https://www.nuget.org/packages/OpenApiFeatureFlags.FeatureManagement) | 0.1.0 | Dogukan Demir | Microsoft.FeatureManagement flag source for OpenApiFeatureFlags: point the libr… |
| 2026-09-30 21:00:55 | [OpenApiFeatureFlags.Abstractions](https://www.nuget.org/packages/OpenApiFeatureFlags.Abstractions) | 0.1.0 | Dogukan Demir | Dependency-free contracts for OpenApiFeatureFlags: the [OpenApiFeatureFlag] att… |
| 2026-09-30 21:00:56 | [OpenApiFeatureFlags](https://www.nuget.org/packages/OpenApiFeatureFlags) | 0.1.0 | Dogukan Demir | Makes an OpenAPI document respect the feature flags the runtime already respect… |
| 2026-09-30 21:09:26 | [PrayerTimePlus](https://www.nuget.org/packages/PrayerTimePlus) | 0.3.0 | abdulwahed-s | Dependency-free Islamic prayer times and Sunnah times for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
