document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("quizForm");
    const progressFill = document.getElementById("progressFill");
    const progressText = document.getElementById("progressText");
    const questionBlocks = document.querySelectorAll(".question-block");

    function updateProgress() {
        let answered = 0;

        questionBlocks.forEach((block) => {
            const checked = block.querySelector('input[type="radio"]:checked');
            if (checked) {
                answered++;
            }
        });

        const total = questionBlocks.length;
        const percentage = Math.round((answered / total) * 100);

        progressFill.style.width = percentage + "%";
        progressText.textContent = percentage + "% completed";
    }

    form.addEventListener("change", updateProgress);
    updateProgress();
});