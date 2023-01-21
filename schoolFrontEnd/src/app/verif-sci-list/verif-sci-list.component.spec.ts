import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerifSciListComponent } from './verif-sci-list.component';

describe('VerifSciListComponent', () => {
  let component: VerifSciListComponent;
  let fixture: ComponentFixture<VerifSciListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VerifSciListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VerifSciListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
