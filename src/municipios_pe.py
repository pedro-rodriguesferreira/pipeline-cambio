import requests


def consultar_municipios(uf: str) -> list | None:
    """Consulta os municípios de uma UF no IBGE. Devolve list ou None se falhar."""

    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.Timeout:
        print(f"[erro] IBGE demorou demais (uf={uf})")
        return None

    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar")
        return None

    except requests.exceptions.HTTPError as erro:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None

if __name__ == "__main__":
    uf = "PE"
    municipios = consultar_municipios(uf)

    if municipios:
        print(f"{uf} tem {len(municipios)} municípios.")
        print(f"\n10 primeiros municípios de {uf}:")
        for municipio in municipios[:10]:
            print(f"  {municipio['nome']}")

    else:
        print(f"[aviso] Nenhum município encontrado para a UF '{uf}' (sigla inválida?)")
