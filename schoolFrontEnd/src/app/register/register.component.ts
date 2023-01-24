import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { Docente } from '../docente';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  name: string = '';
  surname: string= '';
  email: string= '';
  password: string= '';
  errorMessage: string= '';
  successMessage: string= '';
  obsReg: Observable<Docente[]> = undefined!;
  data: any = undefined!;


  constructor(private http: HttpClient, public router: Router) { }

  ngOnInit(): void {
    

  }

  /*register() {
    console.log(".");
    this.obsReg = this.http.post('https://5000-enxo14-schoolexamsproje-cpo672s3qv9.ws-eu83.gitpod.io/register',{ name: this.name, lname: this.lname, email: this.email, password: this.password })
    this.obsReg.subscribe(this.fati)
  }

  fati = (data: Docente[]) => {
    this.data = data;
    console.log(this.data);
    if (Object.keys(this.data).length === 0 || this.data.hasOwnProperty('error')) {
      this.errorMessage = "Error: Invalid Informations!!";
    } else {
      this.successMessage = "You have successfully Registerd!";
      localStorage.setItem('user', JSON.stringify(this.data));
      console.log("2.1");
      this.router.navigate(['/login']);
    }
  }*/
  register() {
    this.http.post('https://5000-enxo14-schoolexamsproje-cpo672s3qv9.ws-eu83.gitpod.io/register',{ name: this.name, surname: this.surname, email: this.email, password: this.password }).subscribe(
      data => {
        console.log(data);
        if (data.hasOwnProperty('error')) {
          this.errorMessage = "Error: Invalid Informations!!";
        } else {
          this.successMessage = "You have successfully Registerd!";
          localStorage.setItem('user', JSON.stringify(data));
          this.router.navigate(['/login']);
        }
      },
      error => {
        console.log(error);
        this.errorMessage = "Error: Invalid Informations!!";
      }
    );
  }
}
