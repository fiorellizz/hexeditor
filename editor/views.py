from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ArquivoBinario
from .forms import UploadForm

# Upload do arquivo
def upload_arquivo(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("editor:visualizar", pk=form.instance.id)
    else:
        form = UploadForm()
    return render(request, "editor/upload.html", {"form": form})

# Exibição do arquivo em Hex Viewer
def visualizar_arquivo(request, pk):
    arquivo = get_object_or_404(ArquivoBinario, pk=pk)
    
    with open(arquivo.arquivo.path, "rb") as f:
        conteudo = f.read()

    hex_view = []
    for i in range(0, len(conteudo), 16):
        linha = conteudo[i:i+16]
        hex_part = []
        ascii_part = ""

        for j, byte in enumerate(linha):
            endereco_real = i + j  # Endereço exato do byte
            byte_hex = f"{byte:02X}"
            
            # Criando link para cada byte
            hex_part.append(f'<a href="/editar/{arquivo.id}/{endereco_real}/">{byte_hex}</a>')

            # Verifica se o byte é imprimível
            ascii_part += chr(byte) if 32 <= byte <= 126 else "."

        hex_view.append({
            "endereco": f"{i:08X}",
            "hex": " ".join(hex_part),  # Bytes agora são links clicáveis
            "ascii": ascii_part
        })

    return render(request, "editor/hex_view.html", {"hex_view": hex_view, "arquivo": arquivo})

# Edição do arquivo
def editar_arquivo(request, pk):
    arquivo = get_object_or_404(ArquivoBinario, pk=pk)

    if request.method == "POST":
        offset = int(request.POST["offset"], 16)
        novo_valor = bytes.fromhex(request.POST["valor"])

        with open(arquivo.arquivo.path, "r+b") as f:
            f.seek(offset)
            f.write(novo_valor)

        return redirect("editor:visualizar", pk=pk)

    return render(request, "editor/editar.html", {"arquivo": arquivo})

# Download do arquivo editado
def download_arquivo(request, pk):
    arquivo = get_object_or_404(ArquivoBinario, pk=pk)
    with open(arquivo.arquivo.path, "rb") as f:
        conteudo = f.read()

    response = HttpResponse(conteudo, content_type="application/octet-stream")
    response["Content-Disposition"] = f'attachment; filename="{arquivo.nome}.bin"'
    return response

def editar_endereco(request, pk, offset):
    arquivo = get_object_or_404(ArquivoBinario, pk=pk)
    offset = int(offset)

    with open(arquivo.arquivo.path, "rb") as f:
        conteudo = f.read()

    if offset >= len(conteudo):
        return HttpResponse("Endereço inválido!", status=400)

    valor_atual = f"{conteudo[offset]:02X}"  # Valor atual em HEX

    if request.method == "POST":
        novo_valor = request.POST.get("novo_valor", "").strip()

        if not novo_valor or len(novo_valor) != 2 or not all(c in "0123456789ABCDEF" for c in novo_valor.upper()):
            return HttpResponse("Valor inválido! Digite um byte válido (ex: FF).", status=400)

        novo_byte = bytes.fromhex(novo_valor)

        # Atualizar o arquivo com o novo valor
        with open(arquivo.arquivo.path, "r+b") as f:
            f.seek(offset)
            f.write(novo_byte)

        return redirect("editor:visualizar", pk=pk)

    return render(request, "editor/editar_endereco.html", {
        "arquivo": arquivo,
        "offset": offset,
        "valor_atual": valor_atual
    })

def editar_byte(request, pk, offset):
    arquivo = get_object_or_404(ArquivoBinario, pk=pk)
    offset = int(offset)

    with open(arquivo.arquivo.path, "rb") as f:
        conteudo = f.read()

    if offset >= len(conteudo):
        return HttpResponse("Endereço inválido!", status=400)

    valor_atual = f"{conteudo[offset]:02X}"  # Valor atual em HEX

    if request.method == "POST":
        novo_valor = request.POST.get("novo_valor", "").strip()

        if not novo_valor or len(novo_valor) != 2 or not all(c in "0123456789ABCDEF" for c in novo_valor.upper()):
            return HttpResponse("Valor inválido! Digite um byte válido (ex: FF).", status=400)

        novo_byte = bytes.fromhex(novo_valor)

        # Atualizar o arquivo com o novo valor
        with open(arquivo.arquivo.path, "r+b") as f:
            f.seek(offset)
            f.write(novo_byte)

        return redirect("editor:visualizar", pk=pk)

    return render(request, "editor/editar_byte.html", {
        "arquivo": arquivo,
        "offset": f"{offset:08X}",
        "valor_atual": valor_atual
    })
