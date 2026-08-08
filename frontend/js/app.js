let selectedMode = "fire";


// ---------------- MODE ---------------- //

function selectMode(mode) {

    selectedMode = mode;

    const fireBtn = document.getElementById("fireBtn");
    const smokingBtn = document.getElementById("smokingBtn");

    fireBtn.classList.remove("active");
    smokingBtn.classList.remove("active");

    if (mode === "fire") {

        fireBtn.classList.add("active");

    } else {

        smokingBtn.classList.add("active");

    }
}


// ---------------- FILE INPUT ---------------- //

const fileInput = document.getElementById("fileInput");
const dropZone = document.getElementById("dropZone");


// Browse button

dropZone.addEventListener("click", function () {

    fileInput.click();

});


// File selected through Windows File Explorer

fileInput.addEventListener("change", function () {

    if (this.files && this.files.length > 0) {

        uploadImage(this.files[0]);

    }

});


// ---------------- DRAG & DROP ---------------- //

dropZone.addEventListener("dragover", function (event) {

    event.preventDefault();

    event.stopPropagation();

    dropZone.classList.add("dragover");

});


dropZone.addEventListener("dragleave", function (event) {

    event.preventDefault();

    dropZone.classList.remove("dragover");

});


dropZone.addEventListener("drop", function (event) {

    event.preventDefault();

    event.stopPropagation();

    dropZone.classList.remove("dragover");


    const files = event.dataTransfer.files;


    if (files && files.length > 0) {

        uploadImage(files[0]);

    }

});


// ---------------- IMAGE UPLOAD ---------------- //

async function uploadImage(file) {

    const status =
        document.getElementById("status");

    const resultSection =
        document.getElementById("resultSection");

    const resultImage =
        document.getElementById("resultImage");


    // Check file type

    const allowedTypes = [
        "image/jpeg",
        "image/png"
    ];


    if (!allowedTypes.includes(file.type)) {

        status.innerText =
            "❌ Please select a JPG, JPEG or PNG image.";

        return;

    }


    // Show processing status

    status.innerText =
        "🔄 Running AI Detection...";


    resultSection.style.display =
        "none";


    // Prepare request

    const formData =
        new FormData();


    formData.append(
        "image",
        file
    );


    formData.append(
        "mode",
        selectedMode
    );


    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/detect/image",
                {
                    method: "POST",
                    body: formData
                }
            );


        if (!response.ok) {

            throw new Error(
                "Server returned an error."
            );

        }


        const blob =
            await response.blob();


        resultImage.src =
            URL.createObjectURL(blob);


        resultSection.style.display =
            "block";


        status.innerText =
            "✅ Detection Completed";


    }

    catch (error) {

        console.error(error);

        status.innerText =
            "❌ Detection failed. Check that Flask is running.";

    }

}