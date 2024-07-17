

export const currentApiKey = async (options) => {
    const apiKey = localStorage.getItem('apiKey')
    if(!apiKey){
        throw new Error('API Key is missing or invalid')
    }
    try {
        //this needs to link to open ai
        const response = await fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify(options)
        })
        
        if(!response.ok){
            throw new Error('Network response issue')
        }
        const data = await response.json()
        return data
    } catch (error) {
        console.error(error)
        throw error
    }
}