import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { flaskLink } from './link';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private baseUrlPrin = flaskLink._API;


  private baseUrl = this.baseUrlPrin + 'users';
  private baseUrl1 = this.baseUrlPrin +'verifSci';

  constructor(private http: HttpClient) { }

  

  getUser(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/${id}`);
  }

  createUser(user: Object): Observable<Object> {
    return this.http.post(`${this.baseUrl}`, user);
  }

  updateUser(id: string, value: any): Observable<Object> {
    return this.http.put(`${this.baseUrl}/${id}`, value);
  }

  deleteUser(id: string): Observable<any> {
    return this.http.delete(`${this.baseUrl}/${id}`, { responseType: 'text' });
  }

  getUsersList(): Observable<any> {
    return this.http.get(`${this.baseUrl}`);
  }
  /** *************************************************************************************************/
  getverifSci(id: string): Observable<any> {
    return this.http.get(`${this.baseUrl1}/${id}`);
  }

  createverifSci(user: Object): Observable<Object> {
    return this.http.post(`${this.baseUrl1}`, user);
  }

  updateverifSci(id: string, value: any): Observable<Object> {
    return this.http.put(`${this.baseUrl1}/${id}`, value);
  }

  deleteverifSci(id: string): Observable<any> {
    return this.http.delete(`${this.baseUrl1}/${id}`, { responseType: 'text' });
  }

  getverifSciList(): Observable<any> {
    return this.http.get(`${this.baseUrl1}`);
  }
}