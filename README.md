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

## Latest list — 2026-09-29 14:19 UTC

New packages created between 2026-09-29 13:21 UTC and 2026-09-29 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T14-19-55-626033Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 13:32:42 | [WrapperPtr](https://www.nuget.org/packages/WrapperPtr) | 1.0.0 | APWMNGP | WrapperPtr is a lightweight C++ pointer wrapper. This library is not a joke lib… |
| 2026-09-29 13:33:07 | [nanoFramework.Iot.Device.Vl53L1X](https://www.nuget.org/packages/nanoFramework.Iot.Device.Vl53L1X) | 1.2.1 | nanoframework | This package includes the .NET IoT Core binding Iot.Device.Vl53L1X for .NET nan… |
| 2026-09-29 13:46:00 | [DecisionKit.Testing](https://www.nuget.org/packages/DecisionKit.Testing) | 0.1.0 | Jonatha Panni | Deterministic test doubles for DecisionKit: fake providers, canned results, req… |
| 2026-09-29 13:46:01 | [DecisionKit.Extensions](https://www.nuget.org/packages/DecisionKit.Extensions) | 0.1.0 | Jonatha Panni | Dependency injection, configuration binding, HttpClientFactory and logging inte… |
| 2026-09-29 13:46:02 | [DecisionKit.Jev](https://www.nuget.org/packages/DecisionKit.Jev) | 0.1.0 | Jonatha Panni | TypeSafe JEV provider for DecisionKit: protocol mapping, HTTP transport, authen… |
| 2026-09-29 13:46:03 | [DecisionKit.Core](https://www.nuget.org/packages/DecisionKit.Core) | 0.1.0 | Jonatha Panni | Provider-independent, strongly typed decision domain model for .NET: questions,… |
| 2026-09-29 13:51:22 | [Arbeidstilsynet.Kommunikasjon.Client](https://www.nuget.org/packages/Arbeidstilsynet.Kommunikasjon.Client) | 0.1.0-alpha2 | Digital Samhandling | Generated Kommunikasjon API client with an adapter, environment-based configura… |
| 2026-09-29 13:58:01 | [Dekaf.Aspire.Hosting](https://www.nuget.org/packages/Dekaf.Aspire.Hosting) | 1.23.0 | Dekaf Contributors | Aspire hosting integration for Apache Kafka and Confluent Schema Registry, with… |
| 2026-09-29 13:58:02 | [Dekaf.Aspire.SchemaRegistry](https://www.nuget.org/packages/Dekaf.Aspire.SchemaRegistry) | 1.23.0 | Dekaf Contributors | Aspire client integration for Dekaf Schema Registry: registers ISchemaRegistryC… |
| 2026-09-29 13:58:03 | [Dekaf.Aspire](https://www.nuget.org/packages/Dekaf.Aspire) | 1.23.0 | Dekaf Contributors | Aspire client integration for Dekaf: registers producers, consumers, share cons… |
| 2026-09-29 13:58:54 | [cl2j.FileStorage.Provider.S3](https://www.nuget.org/packages/cl2j.FileStorage.Provider.S3) | 5.4.0 | CL2J Technologies | S3-compatible object storage provider for cl2j.FileStorage. Works with Amazon S… |
| 2026-09-29 14:01:19 | [Solace.SchemaRegistry.Serdes.Avro](https://www.nuget.org/packages/Solace.SchemaRegistry.Serdes.Avro) | 1.2.0 | Solace Corperation | Solace Avro Schema Registry SERDES for .NET. This includes the following: - Avr… |
| 2026-09-29 14:04:18 | [nanoFramework.Iot.Device.Lis3Dh](https://www.nuget.org/packages/nanoFramework.Iot.Device.Lis3Dh) | 1.0.1 | nanoframework | Binding for the ST LIS3DH ultra-low-power, high-performance three-axis accelero… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
