import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  name: string = '';
  lname: string= '';
  email: string= '';
  password: string= '';
  errorMessage: string= '';
  successMessage: string= '';
  obsReg: Observable<object> | undefined
  data: any = undefined!;


  constructor(private http: HttpClient, public router: Router) { }

  ngOnInit(): void {
    

  }

  register() {
    console.log(".");
    this.obsReg = this.http.post('https://5000-enxo14-schoolexamsproje-cpo672s3qv9.ws-eu83.gitpod.io/register',{ name: this.name, lname: this.lname, email: this.email, password: this.password })
    this.obsReg.subscribe(this.fati)
  }

  fati = (data: object) => {
    this.data = data;
    console.log(this.data);
    if (Object.keys(this.data).length === 0 || this.data.hasOwnProperty('error')) {
      this.errorMessage = "Error: Invalid email or password";
    } else {
      this.successMessage = "You have successfully logged!";
      localStorage.setItem('user', JSON.stringify(this.data));
      console.log("2.1");
      this.router.navigate(['/dashboard']);
    }
  }
}
