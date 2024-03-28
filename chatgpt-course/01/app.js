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