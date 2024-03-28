async function fetchData(){
    const response = await fetch("https://api.openai.com/v1/completions", {
        method: "POST",
        headers: {
            Authorization: `Bearer ${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}`,
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            model: "text-davinci-003",
            prompt: "hello, how are you today?",
            max_token: 7
        })
    })
}