// ================================
// GLOBAL STATE
// ================================

let selectedMode = "fire";
let selectedInput = "image";

let webcamStream = null;

let processingTimer = null;
let processingSeconds = 0;


// ================================
// ELEMENTS
// ================================

const fireMode = document.getElementById("fireMode");
const smokingMode = document.getElementById("smokingMode");

const imageInput = document.getElementById("imageInput");
const videoInput = document.getElementById("videoInput");
const webcamInput = document.getElementById("webcamInput");

const imagePanel = document.getElementById("imagePanel");
const videoPanel = document.getElementById("videoPanel");
const webcamPanel = document.getElementById("webcamPanel");

const readyPanel = document.getElementById("readyPanel");
const processingPanel = document.getElementById("processingPanel");
const resultPanel = document.getElementById("resultPanel");

const pageTitle = document.getElementById("pageTitle");
const pageDescription = document.getElementById("pageDescription");
const modeBadge = document.getElementById("modeBadge");

const systemStatus = document.getElementById("systemStatus");


// ================================
// DETECTION MODE
// ================================

function selectMode(mode) {

    selectedMode = mode;

    fireMode.classList.remove("active");
    smokingMode.classList.remove("active");


    if (mode === "fire") {

        fireMode.classList.add("active");

        pageTitle.innerText = "Fire Detection";

        pageDescription.innerText =
            "Upload an image, video or use your webcam to detect fire using artificial intelligence.";

        modeBadge.innerText = "🔥 Fire";

    } else {

        smokingMode.classList.add("active");

        pageTitle.innerText = "Cigarette Smoking Detection";

        pageDescription.innerText =
            "Detect cigarette smoking using AI-powered computer vision.";

        modeBadge.innerText = "🚬 Smoking";

    }


    resetResults();

}


// ================================
// INPUT SOURCE
// ================================

function selectInput(input) {

    selectedInput = input;


    imageInput.classList.remove("active");
    videoInput.classList.remove("active");
    webcamInput.classList.remove("active");


    imagePanel.classList.add("hidden");
    videoPanel.classList.add("hidden");
    webcamPanel.classList.add("hidden");

    readyPanel.classList.add("hidden");


    stopWebcam();


    if (input === "image") {

        imageInput.classList.add("active");

        imagePanel.classList.remove("hidden");

        pageDescription.innerText =
            "Upload an image to detect fire or cigarette smoking.";

    }


    else if (input === "video") {

        videoInput.classList.add("active");

        videoPanel.classList.remove("hidden");

        pageDescription.innerText =
            "Upload a video for frame-by-frame AI detection.";

    }


    else if (input === "webcam") {

        webcamInput.classList.add("active");

        webcamPanel.classList.remove("hidden");

        pageDescription.innerText =
            "Use your webcam for real-time AI monitoring.";

    }


    resetResults();

}


// ================================
// RESET RESULTS
// ================================

function resetResults() {

    processingPanel.classList.add("hidden");

    resultPanel.classList.add("hidden");

    readyPanel.classList.remove("hidden");

    systemStatus.innerText = "System Ready";

    stopProcessingTimer();

}


// ================================
// IMAGE DRAG & DROP
// ================================

const imageDropZone =
    document.getElementById("imageDropZone");

const imageFileInput =
    document.getElementById("imageFileInput");


imageDropZone.addEventListener(
    "click",
    function () {

        imageFileInput.click();

    }
);


imageFileInput.addEventListener(
    "change",
    function () {

        if (this.files.length > 0) {

            handleImage(this.files[0]);

        }

    }
);


imageDropZone.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        imageDropZone.classList.add("dragover");

    }
);


imageDropZone.addEventListener(
    "dragleave",
    function () {

        imageDropZone.classList.remove("dragover");

    }
);


imageDropZone.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        imageDropZone.classList.remove("dragover");


        if (event.dataTransfer.files.length > 0) {

            handleImage(
                event.dataTransfer.files[0]
            );

        }

    }
);


// ================================
// IMAGE HANDLER
// ================================

function handleImage(file) {

    if (!file.type.startsWith("image/")) {

        showError(
            "Please select a valid image file."
        );

        return;

    }


    const previewURL =
        URL.createObjectURL(file);


    const resultImage =
        document.getElementById("resultImage");


    resultImage.src = previewURL;


    startProcessing();


    /*
        BACKEND CONNECTION WILL BE
        ADDED AFTER THE FLASK API
        IS FIXED.

        For now this only demonstrates
        the complete frontend workflow.
    */


    setTimeout(function () {

        finishProcessing(
            "Image selected successfully. Backend detection will be connected next."
        );

    }, 1000);

}


// ================================
// VIDEO DRAG & DROP
// ================================

const videoDropZone =
    document.getElementById("videoDropZone");

const videoFileInput =
    document.getElementById("videoFileInput");


videoDropZone.addEventListener(
    "click",
    function () {

        videoFileInput.click();

    }
);


videoFileInput.addEventListener(
    "change",
    function () {

        if (this.files.length > 0) {

            handleVideo(this.files[0]);

        }

    }
);


videoDropZone.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        videoDropZone.classList.add("dragover");

    }
);


videoDropZone.addEventListener(
    "dragleave",
    function () {

        videoDropZone.classList.remove("dragover");

    }
);


videoDropZone.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        videoDropZone.classList.remove("dragover");


        if (event.dataTransfer.files.length > 0) {

            handleVideo(
                event.dataTransfer.files[0]
            );

        }

    }
);


// ================================
// VIDEO HANDLER
// ================================

function handleVideo(file) {

    if (!file.type.startsWith("video/")) {

        showError(
            "Please select a valid video file."
        );

        return;

    }


    const video =
        document.getElementById("resultVideo");


    video.src =
        URL.createObjectURL(file);


    document.getElementById(
        "imageResult"
    ).classList.add("hidden");


    document.getElementById(
        "videoResult"
    ).classList.remove("hidden");


    startProcessing();


    /*
        REAL VIDEO DETECTION WILL BE
        CONNECTED TO FLASK LATER.
    */


    simulateProcessing();

}


// ================================
// PROCESSING UI
// ================================

function startProcessing() {

    readyPanel.classList.add("hidden");

    resultPanel.classList.add("hidden");

    processingPanel.classList.remove("hidden");


    systemStatus.innerText =
        "Running Detection";


    document.getElementById(
        "processingStatus"
    ).innerText =
        "AI is processing...";


    processingSeconds = 0;


    document.getElementById(
        "elapsedTime"
    ).innerText =
        "00:00";


    startProcessingTimer();

}


// ================================
// DEMO PROCESSING
// ================================

function simulateProcessing() {

    let progress = 0;

    let frames = 0;

    let objects = 0;


    const interval =
        setInterval(function () {

            progress += 5;

            frames += 12;

            objects =
                Math.floor(
                    Math.random() * 4
                );


            if (progress > 100) {

                progress = 100;

            }


            updateProcessingStats(
                progress,
                frames,
                objects,
                24
            );


            if (progress >= 100) {

                clearInterval(interval);


                finishProcessing(
                    "Video selected successfully. Backend detection will be connected next."
                );

            }

        }, 150);

}


// ================================
// UPDATE PROCESSING
// ================================

function updateProcessingStats(
    progress,
    frames,
    objects,
    fps
) {

    document.getElementById(
        "progressBar"
    ).style.width =
        progress + "%";


    document.getElementById(
        "progressText"
    ).innerText =
        Math.round(progress) + "%";


    document.getElementById(
        "frameCount"
    ).innerText =
        frames;


    document.getElementById(
        "objectCount"
    ).innerText =
        objects;


    document.getElementById(
        "fpsCount"
    ).innerText =
        fps;

}


// ================================
// PROCESSING TIMER
// ================================

function startProcessingTimer() {

    stopProcessingTimer();


    processingTimer =
        setInterval(function () {

            processingSeconds++;


            const minutes =
                Math.floor(
                    processingSeconds / 60
                );


            const seconds =
                processingSeconds % 60;


            document.getElementById(
                "elapsedTime"
            ).innerText =

                String(minutes).padStart(2, "0")
                +
                ":"
                +
                String(seconds).padStart(2, "0");

        }, 1000);

}


function stopProcessingTimer() {

    if (processingTimer !== null) {

        clearInterval(processingTimer);

        processingTimer = null;

    }

}


// ================================
// FINISH PROCESSING
// ================================

function finishProcessing(message) {

    stopProcessingTimer();


    processingPanel.classList.add("hidden");

    resultPanel.classList.remove("hidden");


    systemStatus.innerText =
        "Detection Completed";


    document.getElementById(
        "processingStatus"
    ).innerText =
        "Completed";


    document.getElementById(
        "resultDescription"
    ).innerText =
        message;

}


// ================================
// ERROR
// ================================

function showError(message) {

    stopProcessingTimer();


    processingPanel.classList.add("hidden");

    resultPanel.classList.add("hidden");

    readyPanel.classList.remove("hidden");


    systemStatus.innerText =
        "Error";


    alert(message);

}


// ================================
// WEBCAM
// ================================

const startWebcamButton =
    document.getElementById(
        "startWebcamButton"
    );


const stopWebcamButton =
    document.getElementById(
        "stopWebcamButton"
    );


const webcamVideo =
    document.getElementById(
        "webcamVideo"
    );


const webcamPlaceholder =
    document.getElementById(
        "webcamPlaceholder"
    );


startWebcamButton.addEventListener(
    "click",
    startWebcam
);


stopWebcamButton.addEventListener(
    "click",
    stopWebcam
);


async function startWebcam() {

    try {

        webcamStream =
            await navigator.mediaDevices.getUserMedia({
                video: true,
                audio: false
            });


        webcamVideo.srcObject =
            webcamStream;


        webcamVideo.style.display =
            "block";


        webcamPlaceholder.style.display =
            "none";


        systemStatus.innerText =
            "Camera Active";


        /*
            REAL YOLO WEBCAM DETECTION
            WILL BE CONNECTED LATER.
        */

    }

    catch (error) {

        console.error(error);


        showError(
            "Camera access was denied or is unavailable."
        );

    }

}


function stopWebcam() {

    if (webcamStream) {

        webcamStream
            .getTracks()
            .forEach(
                track => track.stop()
            );


        webcamStream = null;

    }


    if (webcamVideo) {

        webcamVideo.srcObject = null;

        webcamVideo.style.display =
            "none";

    }


    if (webcamPlaceholder) {

        webcamPlaceholder.style.display =
            "block";

    }

}


// ================================
// DOWNLOAD BUTTON
// ================================

const downloadButton =
    document.getElementById(
        "downloadButton"
    );


downloadButton.addEventListener(
    "click",
    function () {

        const resultImage =
            document.getElementById(
                "resultImage"
            );


        const resultVideo =
            document.getElementById(
                "resultVideo"
            );


        if (
            !resultImage.classList.contains("hidden")
            &&
            resultImage.src
        ) {

            downloadFile(
                resultImage.src,
                "detection-result.png"
            );

        }


        else if (
            !resultVideo.classList.contains("hidden")
            &&
            resultVideo.src
        ) {

            downloadFile(
                resultVideo.src,
                "detection-result.mp4"
            );

        }

    }
);


// ================================
// DOWNLOAD HELPER
// ================================

function downloadFile(
    url,
    filename
) {

    const link =
        document.createElement("a");


    link.href = url;

    link.download = filename;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

}