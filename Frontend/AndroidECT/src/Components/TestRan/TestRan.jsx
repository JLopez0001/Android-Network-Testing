function TestRan({testNames}) {
  return (
    <div>
        <h5>Test Name:</h5>
        <ul>
            {testNames?.map((names, index) => (
                <li key={index}>{names}</li>
            ))}
        </ul>
    </div>
  )
}

export default TestRan