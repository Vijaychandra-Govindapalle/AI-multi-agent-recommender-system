'use client'

import { useState } from 'react'

export default function Home() {
  const [customerId, setCustomerId] = useState('')
  const [recommendations, setRecommendations] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const fetchRecommendations = async () => {
    setLoading(true)
    setError('')
    setRecommendations([])
  
    try {
      const res = await fetch(`http://localhost:8000/recommend?timestamp=${Date.now(), { cache: 'no-store' }}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ customer_id: customerId.trim().toUpperCase() })
      })
      
  
      const data = await res.json()
      console.log('Received Data:', data)
  
      if (res.ok) {
        setRecommendations(data.recommendations || [])
      } else {
        setError(data.detail || 'Something went wrong')
      }
    } catch (err) {
      console.error(err)
      setError('Error fetching recommendations')
    } finally {
      setLoading(false)
    }
  }
  

  return (
    <main className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-2xl bg-white rounded-2xl shadow-md p-8">
        <h1 className="text-3xl font-bold mb-4 text-center text-blue-500">AI Product Recommender</h1>

        <p className="text-sm text-gray-600 mb-2">
          <strong>Instruction:</strong> Please enter the Customer ID in the following format: <code className="bg-gray-200 px-2 py-0.5 rounded text-sm">C1001</code> up to <code className="bg-gray-200 px-2 py-0.5 rounded text-sm">C10999</code>.
        </p>

        <input
          type="text"
          placeholder="Enter Customer ID (e.g., C1001)"
          value={customerId}
          onChange={(e) => setCustomerId(e.target.value)}
          className="w-full px-4 py-2 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400 text-blue-500"
        />

        <button
          onClick={fetchRecommendations}
          className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 rounded-lg transition"
          disabled={loading || !customerId}
        >
          {loading ? 'Loading...' : 'Get Recommendations'}
        </button>

        {error && <p className="text-red-500 text-sm mt-4">{error}</p>}

        {recommendations.length > 0 && (
          <div className="mt-6 space-y-3">
            <h2 className="text-xl font-semibold text-center text-green-400">Recommended Products</h2>
            {recommendations.map((rec: any, idx) => (
              <ProductCard key={idx} rec={rec} />
          ))}

          </div>
        )}

        <div className="mt-10">
          <h3 className="text-lg font-semibold mb-2 text-center text-yellow-400">Sample Customers for Testing</h3>
          <div className="overflow-x-auto">
            <table className="table-auto w-full text-sm border border-gray-300">
              <thead className="bg-red-300">
                <tr className='text-white'>
                  <th className="px-2 py-1 border">Customer ID</th>
                  <th className="px-2 py-1 border">Age</th>
                  <th className="px-2 py-1 border">Gender</th>
                  <th className="px-2 py-1 border">City</th>
                  <th className="px-2 py-1 border">Interests</th>
                </tr>
              </thead>
              <tbody className='text-blue-400'>
                <tr><td className="border px-2 py-1">C10996</td><td className="border">34</td><td className="border">Other</td><td className="border">Delhi</td><td className="border">Beauty</td></tr>
                <tr><td className="border px-2 py-1">C9320</td><td className="border">60</td><td className="border">Female</td><td className="border">Kolkata</td><td className="border">Books</td></tr>
                <tr><td className="border px-2 py-1">C8395</td><td className="border">50</td><td className="border">Male</td><td className="border">Delhi</td><td className="border">Electronics</td></tr>
                <tr><td className="border px-2 py-1">C3020</td><td className="border">33</td><td className="border">Other</td><td className="border">Delhi</td><td className="border">Fitness, Home Decor, Beauty</td></tr>
                <tr><td className="border px-2 py-1">C2394</td><td className="border">35</td><td className="border">Other</td><td className="border">Delhi</td><td className="border">Home Decor, Books</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </main>
  )
}

function ProductCard({ rec }: { rec: any }) {
  const [showMore, setShowMore] = useState(false)
  console.log("Rendering Recommendation:", rec)


  return (
    <div className="bg-gray-50 p-4 rounded-lg shadow-sm border mb-4">
      <div className="flex flex-wrap gap-4 justify-between items-center text-sm font-medium text-blue-700">
        <span>🆔 {rec.Product_ID}</span>
        <span>📦 {rec.Subcategory}</span>
        <span>📁 {rec.Category}</span>
        <span>💰 ₹{rec.Price}</span>
        <span>⭐ {rec.Product_Rating}</span>
      </div>

      <button
        onClick={() => setShowMore(!showMore)}
        className="mt-2 text-sm text-blue-500 hover:underline"
      >
        {showMore ? 'Hide Details ▲' : 'View More ▼'}
      </button>

      {showMore && (
  <div className="mt-3 text-sm text-gray-600 space-y-1">
    <p>Brand: {rec.Brand}</p>
    <p>Avg. Rating (Similar Products): {rec.Average_Rating_of_Similar_Products}</p>
    <p>Review Sentiment Score: {rec.Customer_Review_Sentiment_Score}</p>
    <p>Season: {rec.Season}</p>
    <p>Location: {rec.Geographical_Location}</p>
    <p>Holiday Recommended: {rec.Holiday}</p>
    <p>Probability of Recommendation: {rec.Probability_of_Recommendation}</p>
    <p>
      Similar Products:{' '}
      {Array.isArray(rec.Similar_Product_List)
        ? rec.Similar_Product_List.join(', ')
        : String(rec.Similar_Product_List || 'N/A')}
    </p>
  </div>
)}

    </div>
  )
}

export const dynamic = 'force-dynamic'
