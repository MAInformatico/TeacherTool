import React from 'react'

class Form extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        reading: '',
        listening: '',
        speaking: '',
        writing: '',
        use_of_english: ''
      };
    }
  
    handleSubmit = (event) => {
      event.preventDefault();
      alert('Examenes enviados');
    };
  
    render() {
      return (
        <div className="Form">
        <form onSubmit={this.handleSubmit}>
          <tr>
          <label>
            Reading:<input
              type="text"
              value={this.state.reading}
              onChange={(e) => this.setState({ reading: e.target.value })}
            />
          </label>
          </tr>
          <tr>
          <label>
            Listening:<input type="text"
              value={this.state.listening}
              onChange={(e) => this.setState({ listening: e.target.value })}
            />
          </label>
          </tr>
          <tr>
          <label>
            Speaking:<input
              type="text"
              value={this.state.speaking}
              onChange={(e) => this.setState({ speaking: e.target.value })}
            />
          </label>
          </tr>
          <tr>
          <label>
            Writing:<input
              type="text"
              value={this.state.writing}
              onChange={(e) => this.setState({ writing: e.target.value })}
            />
          </label>
          </tr>
          <tr>
          <label>
            Use of English:<input
              type="text"
              value={this.state.use_of_english}
              onChange={(e) => this.setState({ use_of_english: e.target.value })}
            />
          </label>
          </tr>
          <tr>
          <button type="submit" onClick={() => alert("Examenes enviados")}>Enviar</button>
          <button type="button" onClick={() => this.setState({ reading: '', listening: '', speaking: '', writing: '', use_of_english: '' })}>Limpiar</button>
          </tr>
        </form>
        </div>
      );
    }
  }
export default Form;