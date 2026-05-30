document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const ideaInput = document.getElementById('idea-input');
    const loadingOverlay = document.getElementById('loading-overlay');
    const resultsSection = document.getElementById('results-section');
    const summaryContent = document.getElementById('summary-content');
    const tabPaneContent = document.getElementById('tab-pane-content');
    const tabLinks = document.querySelectorAll('.tab-link');

    let currentResults = null;

    analyzeBtn.addEventListener('click', async () => {
        const idea = ideaInput.value.trim();
        
        if (!idea) {
            alert('Please enter your startup idea first!');
            return;
        }

        // Show loading state
        loadingOverlay.classList.remove('hidden');
        resultsSection.classList.add('hidden');
        analyzeBtn.disabled = true;

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ idea }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Analysis failed');
            }

            const data = await response.json();
            currentResults = data;
            
            displayResults(data);
        } catch (error) {
            console.error('Error:', error);
            alert(`Error: ${error.message}`);
        } finally {
            loadingOverlay.classList.add('hidden');
            analyzeBtn.disabled = false;
        }
    });

    function displayResults(data) {
        resultsSection.classList.remove('hidden');
        
        // Render Summary
        summaryContent.innerHTML = marked.parse(data.summary);

        // Show first tab by default
        showTab(0);

        // Smooth scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function showTab(index) {
        // Update active tab link
        tabLinks.forEach(link => link.classList.remove('active'));
        const activeLink = document.querySelector(`.tab-link[data-tab="${index}"]`);
        if (activeLink) activeLink.classList.add('active');

        // Update content
        if (currentResults && currentResults.tasks[index]) {
            const task = currentResults.tasks[index];
            tabPaneContent.innerHTML = `
                <div class="agent-badge">Agent: ${task.agent}</div>
                ${marked.parse(task.raw)}
            `;
        }
    }

    // Tab Event Listeners
    tabLinks.forEach(link => {
        link.addEventListener('click', () => {
            const index = parseInt(link.getAttribute('data-tab'));
            showTab(index);
        });
    });
});
