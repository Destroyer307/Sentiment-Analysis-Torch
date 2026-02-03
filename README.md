# Hugging Face ile Yerel LLM Chatbot

Bu proje, Hugging Face Transformers kütüphanesi kullanılarak geliştirilmiş
basit bir yerel chatbot uygulamasıdır.

Projenin amacı bir chatbot yapmak kadar,
Büyük Dil Modellerinin (LLM) *prompt, **input, **output* ve *response*
kavramlarını nasıl işlediğini derinlemesine anlamaktır.

## Bu Proje Ne Gösteriyor?

- Prompt, input, output ve response arasındaki farklar
- Chat template (apply_chat_template) mantığı
- Model çıktılarının neden hem prompt hem cevap içerdiği
- Model cevabının output içinden nasıl ayrıştırıldığı
- Temperature, top-p ve sampling gibi üretim parametrelerinin etkisi

## Temel Kavramlar

### Prompt
Prompt sadece kullanıcının sorduğu soru değildir.
Şunları içerir:
- System mesajı (modelin nasıl davranacağını söyler)
- Önceki konuşmalar (varsa)
- Kullanıcı sorusu
- Assistant cevap üretme etiketi

### Inputs
Inputs, prompt’un tokenize edilmiş (sayılara çevrilmiş) halidir.
Modelin gerçekten gördüğü şey budur.

### Outputs
Model çıktısı şunları içerir:
- Prompt’a ait tokenlar
- Modelin ürettiği cevap tokenları

Model input ve cevabı otomatik olarak ayırmaz.

### Response
Gerçek cevap, output içinden prompt tokenları çıkarılarak elde edilir.
Bu işlem:
- Prompt uzunluğu hesaplanarak
- Output dizisi dilimlenerek
- Kalan tokenlar decode edilerek yapılır

## Kullanılan Model
TinyLlama/TinyLlama-1.1B-Chat-v1.0

Bu model, hafif olduğu ve CPU üzerinde çalışabildiği için tercih edilmiştir.

## Çalıştırma

```bash
pip install torch transformers
python Sample_Chatbot_1.py
