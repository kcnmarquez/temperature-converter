document.querySelectorAll('input').forEach(temperatureInput => {
    temperatureInput.addEventListener('input', async (e) => {
        const desiredUnit = e.target.dataset.desiredUnit;
        const tempValue = e.target.value;

        if (!tempValue) {
            setOtherInput(desiredUnit, '');
            return;
        };
    
        const response = await fetch('/convert/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: tempValue, desired_unit: desiredUnit}),
        });
        const result = await response.json();
        
        setOtherInput(desiredUnit, result.result);
    });
});

function setOtherInput(desiredUnit, value) {
    const desiredUnitInput = document.querySelector(`input:not([data-desired-unit="${desiredUnit}"])`);
    desiredUnitInput.value = value;
}