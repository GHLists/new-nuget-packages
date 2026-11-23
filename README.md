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

## Latest list — 2026-11-23 02:21 UTC

New packages created between 2026-11-23 01:20 UTC and 2026-11-23 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T02-21-34-20146Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 01:24:06 | [CodeBrix.WebPlatform.Styling.Tailwind4.LinuxArm64.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.LinuxArm64.MitLicenseForever) | 1.0.327.82 | Jeremy Ellis | The prebuilt standalone Tailwind CSS 4.3.5 program (tailwindcss) for Linux Arm6… |
| 2026-11-23 01:24:45 | [CodeBrix.WebPlatform.Styling.Tailwind4.LinuxX64.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.LinuxX64.MitLicenseForever) | 1.0.327.82 | Jeremy Ellis | The prebuilt standalone Tailwind CSS 4.3.5 program (tailwindcss) for Linux x64… |
| 2026-11-23 01:24:47 | [HybridModelBinding2](https://www.nuget.org/packages/HybridModelBinding2) | 1.0.0 | Bill Boga,David Grieve | Bind one ASP.NET Core MVC model from the request body, form, route, query strin… |
| 2026-11-23 01:25:18 | [CodeBrix.WebPlatform.Styling.Tailwind4.MacOSArm64.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.MacOSArm64.MitLicenseForever) | 1.0.327.82 | Jeremy Ellis | The prebuilt standalone Tailwind CSS 4.3.5 program (tailwindcss) for macOS Arm6… |
| 2026-11-23 01:25:56 | [CodeBrix.WebPlatform.Styling.Tailwind4.MacOSX64.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.MacOSX64.MitLicenseForever) | 1.0.327.82 | Jeremy Ellis | The prebuilt standalone Tailwind CSS 4.3.5 program (tailwindcss) for macOS x64… |
| 2026-11-23 01:26:41 | [CodeBrix.WebPlatform.Styling.Tailwind4.Sources](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.Sources) | 1.0.327.82 | Jeremy Ellis | The source code of the prebuilt standalone Tailwind CSS 4.3.5 programs that the… |
| 2026-11-23 01:27:30 | [CodeBrix.WebPlatform.Styling.Tailwind4.WindowsX64.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.Styling.Tailwind4.WindowsX64.MitLicenseForever) | 1.0.327.82 | Jeremy Ellis | The prebuilt standalone Tailwind CSS 4.3.5 program (tailwindcss) for Windows x6… |
| 2026-11-23 01:36:55 | [ZFormat](https://www.nuget.org/packages/ZFormat) | 2.0.0 | Cristobal Rodas | Biblioteca de C# para crear interfaces de consola con controles, paneles, tabla… |
| 2026-11-23 01:54:38 | [SyntaxCircus.Maui.StoreReview](https://www.nuget.org/packages/SyntaxCircus.Maui.StoreReview) | 0.1.0 | Syntax Circus LLC | In-app review prompts and store write-review links for MAUI apps on iOS (SKStor… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
