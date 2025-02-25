var plants =new Vue({
    el: '#app',
    data: {
      image: null,
      result: '',
      imageUrl: '',
      loading: true
    },
    methods: {
      handleFileUpload(event) {
        this.image = event.target.files[0];
      },
      uploadImage() {
        this.loading = true;
        if (!this.image) {
          alert('Please select an image.');
          return;
        }
        let formData = new FormData();
        formData.append('image', this.image);
  
        fetch('/upload', {
          method: 'POST',
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          if(data.result){
            plants.result = data.result;
          }
          // Display the image from static/uploads folder
          this.imageUrl = '/static/uploads/' + data.filename;
          console.log(this.imageUrl);
          console.log(this.result);
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }
    }
  });  