import React, {useEffect} from 'react';
import './App.css';
import List from './Test/List'


function App() {
  let [todos , setTodos] = React.useState([{

  }])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/products')
      .then(response => response.json())
      .then(_todos => setTodos(_todos))  
  }, [])


  return (
      <div className='container'>
        <List props = { todos }/>
      </div>
    )
}

export default App;
