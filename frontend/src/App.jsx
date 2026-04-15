import { useEffect, useState } from 'react'

function App() {
  const [productos, setProductos] = useState([])

  useEffect(() => {
    

    //Backend (FastAPI) corriendo en el puerto 8000
    fetch('http://localhost:8000/items')
      .then(response => response.json())
      .then(data => {
        console.log("Datos recibidos:", data)
        setProductos(data)
      })
      .catch(error => console.error("Error conectando al Backend:", error))
  }, [])
  

  return (
    <div style={{ padding: '20px', backgroundColor: '#f0f2f5', minHeight: '100vh', fontFamily: 'Arial' }}>
      <h1 style={{ color: '#1a73e8' }}>Innovatech Chile - Panel de Control</h1>
      <hr />
      <h3>Listado de Productos (Desde Capa Data - Supabase)</h3>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {productos.length > 0 ? (
          productos.map((item) => (
            <div key={item.id} style={{ background: 'white', padding: '15px', borderRadius: '5px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <strong>Producto:</strong> {item.nombre} | <strong>Precio:</strong> ${item.precio}
            </div>
          ))
        ) : (
          <p>Cargando datos o verificando conexión con el Backend...</p>
        )}
      </div>
    </div>
  )
}

export default App