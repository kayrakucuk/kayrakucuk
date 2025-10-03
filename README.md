## Docker MCP Sunucusu Örneği

Bu depo, Docker içinde çalıştırılabilen basit bir [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) sunucusu örneği içerir.

### Başlangıç

Detaylı yönergeler için [`docker-mcp/README.md`](docker-mcp/README.md) dosyasına göz atabilirsiniz. Kısaca, proje dizinine gidip aşağıdaki komutlarla imajı oluşturup konteyneri çalıştırabilirsiniz:

```bash
cd docker-mcp
docker build -t docker-mcp-server .
docker run --rm -p 8000:8000 docker-mcp-server
```

Sunucu örnek olarak iki araç sağlar: bir selamlama (`hello`) ve anlık UTC zamanı döndüren (`server_time`). Bu iskeleti kendi ihtiyaçlarınıza göre genişletebilirsiniz.
