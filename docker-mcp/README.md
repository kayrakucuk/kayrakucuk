# Docker MCP Server

Bu klasör, Docker kullanarak basit bir Model Context Protocol (MCP) sunucusu çalıştırmak için örnek içerir.

## Projeyi Çalıştırma

1. **Docker imajını oluşturun:**

   ```bash
   docker build -t docker-mcp-server .
   ```

2. **Konteyneri başlatın:**

   ```bash
   docker run --rm -p 8000:8000 docker-mcp-server
   ```

   Konteyner çalıştığında MCP sunucusu `8000` portu üzerinden istekleri dinleyecektir.

## MCP Araçları

Sunucu aşağıdaki iki örnek aracı sağlar:

- `hello`: Parametre olarak verilen isme selam verir.
- `server_time`: Sunucu saati olarak güncel UTC zaman damgasını döndürür.

Bu örnek, kendi MCP araçlarınızı geliştirmek için başlangıç noktası olarak kullanılabilir.
