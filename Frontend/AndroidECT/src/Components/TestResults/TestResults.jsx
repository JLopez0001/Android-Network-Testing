function TestResults({testResults}) {
  return (
    <div>
        <h5>TestResults</h5>
        <ul>
            {testResults?.map((results, index) => (
                <li key={index}>{results}</li>
            ))}
        </ul>
    </div>
  )
}

export default TestResults