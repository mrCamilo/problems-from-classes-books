import React, {Component} from 'react'

class MemeGenerator extends Component {
    constructor() {
	    super()
	    this.state = {
	        topText: "",
		bottomText: "",
		randomImg: "http://i.imgflip.com/1bij.jpg",
		allMemeImgs: []
	    }

	    this.handleChange = this.handleChange.bind(this)
    	    this.handleSubmit = this.handleSubmit.bind(this)
    }

	    componentDidMount() {
	        fetch("https://api.imgflip.com/get_memes")
		    .then(res => res.json())
		    .then(res => {
			const {memes} = res.data
			this.setState({ allMemeImgs: memes })
		    })
    }

    handleChange (event) {
	const {name, value} = event.target
	this.setState( { [name]: value } )
    }

    handleSubmit(event) {
	    event.preventDefault()
   	    const rand = Math.floor(Math.random() * this.state.allMemeImgs.length)
	    const randMemeImg = this.state.allMemeImgs[rand].url
	    this.setState({ randomImg: randMemeImg })
    }
	
    render(){
        return (
            <div>
		<form className="meme-form">
		    <input
			type = "text"
			name = "topText"
			placeholder = "Top Text"
			value = {this.state.topText}
			onChange = {this.handleChange}
		    />

		    <input
		        type = "text"
		        name = "bottomText"
		        placeholder = "Bottom Text"
			value = {this.state.bottomText}
			onChange = {this.handleChange}
		    />

		    <button>Gen</button>
		</form>


	<div className="meme">
		<img src= {this.state.randomImg} alt="" />
		<h2 className="top">{this.state.topText}</h2>
		<h2 className="bottom">{this.state.bottomText}</h2>
	</div>

	    </div>
	)
    }
}

export default MemeGenerator
