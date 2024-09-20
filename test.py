from pywebpush import webpush, WebPushException
import json

# VAPID keys should only be generated once.
vapid_private_key = "MPQ5syPiI_5gwJdIBpoWT7EKOEzLTYnCSePBWV7Xi4w"
vapid_claims = {
    "sub": "mailto:example@yourdomain.org"
}

# This is the same output of calling JSON.stringify on a PushSubscription
push_subscription = {
    "endpoint": "https://wns2-pn1p.notify.windows.com/w/?token=BQYAAAAa2NfLES1dB4wSkivyqfP%2bjSDaD1i1WVLud6pElC53iJ7nFsxFst%2bhSFIOeZhfb8sO%2fBLg%2bnFSmqgyX3PwJybXkFQVAFAxh614Fay5XpIMNjPj6yo2MDIPpSV5qzLMpG5CIBm0xog5%2fXePeEwPuKrZ4dT71yKAeejkkVrWfrfC3FbGfuVlwALdRMtiirlTHccRZRJlhBAU33FZd15triAb96oPOD%2bqviwb%2bTKzcEhoOJzV65ET%2fLDd72FNUjVea%2fQOzQK1qa%2b62L1ih%2fzsWRWZD7EuPY38padtbqOCb4G%2fX0dHzPRCUV5yhBthSxJ6%2fujtj2GHjaAzx6wUNGF6I7dn",
    "keys": {
        "auth": "jd5BBNuU_qundsnKTVeNhw",
        "p256dh": "BB8L4yx9YhTmnblIsLeVS2I1yvDaYXBWBJeQrZCdnhfNTEXrPpgeQnRgBfDcV7VYa6AdR_vxfU8v_C0gUIEcwIQ",
    }
}

try:
    webpush(
        subscription_info=push_subscription,
        data=json.dumps({"title": "hello", "body": "Nhân"}),
        vapid_private_key=vapid_private_key,
        vapid_claims=vapid_claims
    )
except WebPushException as ex:
    print("I'm sorry, but the push subscription is invalid:", repr(ex))
    # Mozilla returns additional information in the body of the response.
    if ex.response and ex.response.json():
        extra = ex.response.json()
        print("Remote service replied with a {}:{}, {}",
              extra.code,
              extra.errno,
              extra.message
              )