document.getElementById("qrForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let formData = new FormData(this);

    fetch("/generate_qr", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        let imgUrl = URL.createObjectURL(blob);
        let qrImage = document.getElementById("qrImage");
        let qrContainer = document.getElementById("qrContainer");
        let qrBox = document.querySelector(".qr-box");
        let downloadBtn = document.getElementById("downloadBtn");

        qrImage.src = imgUrl;
        qrImage.style.display = "block";

        qrContainer.style.display = "flex";
        setTimeout(() => {
            qrBox.style.opacity = "1";
            qrBox.style.transform = "translateY(0)";
        }, 100);

        downloadBtn.style.display = "inline-block";
        downloadBtn.onclick = function() {
            let a = document.createElement("a");
            a.href = imgUrl;
            a.download = "qr_code.png";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        };
    })
    .catch(error => console.error("Error:", error));
});
