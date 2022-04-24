import React from 'react'
import './style.css'
import 'bootstrap/dist/css/bootstrap.min.css'

export default function List({ props }) { 
	if(props.length > 1){
		return (
			<ul>
				{props.map((e) => (
					<li>
						<div className = 'alert-primary'>
							<h1>{e.name}</h1>
							<p>Price: {e.price}$</p>
						</div>
					</li>
				))}
			</ul>
		)
	}

	return <h2>Products not found!</h2>

}

