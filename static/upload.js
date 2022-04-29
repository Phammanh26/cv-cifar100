const handleImageUpload = event => {
    console.log('hello')
    const files = event.target.files
    const formData = new FormData()
    formData.append('image', files[0])
  
    fetch('/test', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {

      console.log(data)
    })
    .catch(error => {
      console.error(error)
    })
  }
  
  document.querySelector('#fileUpload').addEventListener('change', event => {
    handleImageUpload(event)
  })