/**
 * Main frontend application JavaScript
 */

document.addEventListener("DOMContentLoaded", () => {
  const healthCheckBtn = document.getElementById("health-check");
  const getItemsBtn = document.getElementById("get-items");
  const responseContainer = document.getElementById("api-response");

  /**
   * Display API response in the UI
   */
  function displayResponse(data, status = "success") {
    responseContainer.innerHTML = `
      <div class="response ${status}">
        <h4>Response:</h4>
        <pre>${JSON.stringify(data, null, 2)}</pre>
      </div>
    `;
    responseContainer.classList.remove("hidden");
  }

  /**
   * Display error message
   */
  function displayError(message) {
    responseContainer.innerHTML = `
      <div class="response error">
        <h4>Error:</h4>
        <p>${message}</p>
      </div>
    `;
    responseContainer.classList.remove("hidden");
  }

  /**
   * Check API health
   */
  async function checkHealth() {
    try {
      const response = await fetch("/api/v1/health");
      const data = await response.json();
      displayResponse(data, response.ok ? "success" : "error");
    } catch (error) {
      displayError(`Failed to connect to API: ${error.message}`);
    }
  }

  /**
   * Get items from API
   */
  async function getItems() {
    try {
      const response = await fetch("/api/v1/items");
      const data = await response.json();
      displayResponse(data, response.ok ? "success" : "error");
    } catch (error) {
      displayError(`Failed to fetch items: ${error.message}`);
    }
  }

  // Event listeners
  if (healthCheckBtn) {
    healthCheckBtn.addEventListener("click", checkHealth);
  }

  if (getItemsBtn) {
    getItemsBtn.addEventListener("click", getItems);
  }

  // Auto-check health on load
  checkHealth();
});
