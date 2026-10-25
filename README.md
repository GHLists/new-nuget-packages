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

## Latest list — 2026-10-25 00:21 UTC

New packages created between 2026-10-24 23:20 UTC and 2026-10-25 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T00-21-52-292217Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 23:26:02 | [DotNetPip](https://www.nuget.org/packages/DotNetPip) | 1.0.0 | Jaime Olivares | Universal In-Process C# - Python Interoperability Engine for .NET 10 |
| 2026-10-24 23:27:34 | [KDesktop.Assistant.Sdk](https://www.nuget.org/packages/KDesktop.Assistant.Sdk) | 1.0.0 | Kobayashi82 | The SDK for writing assistants for K-Desktop: characters that live on top of yo… |
| 2026-10-24 23:27:36 | [KDesktop.Assistant.Templates](https://www.nuget.org/packages/KDesktop.Assistant.Templates) | 1.0.0 | Kobayashi82 | dotnet new template for a K-Desktop assistant (kdassistant): the smallest compl… |
| 2026-10-24 23:37:46 | [KatziDrip](https://www.nuget.org/packages/KatziDrip) | 1.0.8 | AaronoLW | Theme library for Katzi software |
| 2026-10-24 23:38:50 | [Bts.Login.AspNetCore](https://www.nuget.org/packages/Bts.Login.AspNetCore) | 1.0.1 | Bellga Tech Solutions | "Entrar com BTS" para sites e APIs ASP.NET Core: login OpenID Connect com PKCE… |
| 2026-10-24 23:38:51 | [Bts.Login.Cliente](https://www.nuget.org/packages/Bts.Login.Cliente) | 1.0.1 | Bellga Tech Solutions | "Entrar com BTS" para apps (.NET, MAUI, desktop): Authorization Code + PKCE pel… |
| 2026-10-24 23:38:53 | [Bts.Login.Maui](https://www.nuget.org/packages/Bts.Login.Maui) | 1.0.1 | Bellga Tech Solutions | "Entrar com BTS" para apps .NET MAUI: login pelo navegador do sistema (WebAuthe… |
| 2026-10-24 23:49:29 | [Vanara.PInvoke.WebAuthn](https://www.nuget.org/packages/Vanara.PInvoke.WebAuthn) | 5.0.8 | David Hall | PInvoke API (methods, structures and constants) imported from the WebAuthn API. |
| 2026-10-24 23:57:24 | [VertaIT.WPF.NetTheme](https://www.nuget.org/packages/VertaIT.WPF.NetTheme) | 1.0.0 | Verta IT | Free and easy-to-use light and dark themes for WPF applications |
| 2026-10-24 23:57:24 | [VertaIT.WPF.Theme](https://www.nuget.org/packages/VertaIT.WPF.Theme) | 1.0.0 | Verta IT | Free and easy-to-use light and dark themes for WPF applications |
| 2026-10-25 00:06:23 | [IBKR.Net](https://www.nuget.org/packages/IBKR.Net) | 0.1.0 | LimitlessSoft | A from-scratch .NET client for the Interactive Brokers TWS / IB Gateway socket… |
| 2026-10-25 00:06:24 | [IBKR.Net.Contracts](https://www.nuget.org/packages/IBKR.Net.Contracts) | 0.1.0 | LimitlessSoft | Models and options of IBKR.Net, a from-scratch client for the Interactive Broke… |
| 2026-10-25 00:10:59 | [Tharga.Team.Support.Anthropic](https://www.nuget.org/packages/Tharga.Team.Support.Anthropic) | 4.4.0 | Daniel Bohlin | Lets each team's support assistant answer through its own Neurolito key, over t… |
| 2026-10-25 00:12:50 | [Shaderlyn.CFamily](https://www.nuget.org/packages/Shaderlyn.CFamily) | 0.3.0 | OmojiP | Shaderlyn の C 系のシェーダー言語 (HLSL / GLSL / Slang など) に共通の部分。字句解析、トークン、プリプロセッサ、取り込みの… |
| 2026-10-25 00:12:55 | [Shaderlyn.Glsl](https://www.nuget.org/packages/Shaderlyn.Glsl) | 0.3.0 | OmojiP | Shaderlyn の GLSL の構文解析 (GLSL に固有の構文)。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
