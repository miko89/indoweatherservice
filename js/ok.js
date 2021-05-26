
        function submitData(){
            var nama = document.getElementById("nama").value;
            var email = document.getElementById("email").value;
            var address = document.getElementById("address").value;
            var city = document.getElementById("city").value;
            var country = document.getElementById("country").value;
            var sex = document.querySelector('input[name="sex"]:checked').value;
            var berlangganan = document.getElementById("berlangganan").checked;

            var json = {
                name: nama,
                email: email,
                address: address,
                city: city,
                country: country,
                sex: sex,
                subscription: berlangganan         
            }
            console.log(json);


           // return false;
        }
    